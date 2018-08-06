import logging
from define import SCREEN_FEATURES, MINIMAP_FEATURES, ACTIONS

import sys
from absl import flags

from pysc2.env import sc2_env
from pysc2.env.environment import StepType
from pysc2.lib import actions

import numpy as np

__author__ = 'lizhihao6'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class SC2GameEnv():

    def __init__(self, **kwargs):

        FLAGS = flags.FLAGS
        FLAGS(sys.argv)
        self.env = sc2_env.SC2Env(**kwargs)
        self.episode = 0
        self.num_step = 0
        self.episode_reward = 0
        self.total_reward = 0
        self.screen_size = self.env.observation_spec()["screen"][1:]
        self.minimap_size = self.env.observation_spec()["minimap"][1:]
        self.minimap_size = None

    def step(self, action):

        try:
            obs = self.env.step(
                [actions.FunctionCall(action[0], action[1:])])[0]
        except KeyboardInterrupt:
            logger.info("Interrupted. Quitting...")
            return None, 0, True, {}
        except Exception:
            logger.exception(
                "An unexpected error occurred while applying action to environment.")
            return None, 0, True, {}

        state, useless_state = self.obs2state(obs)
        reward = obs.reward
        done = (obs.step_type == StepType.LAST)
        self.num_step += 1
        self.episode_reward += reward
        self.total_reward += reward

        return state, reward, done, useless_state

    def reset(self):

        if self.episode > 0:
            logger.info("Episode %d ended with reward %d after %d steps.",
                        self.episode, self.episode_reward, self.num_step)
            logger.info("Got %d total reward so far, with an average reward of %g per episode",
                        self.total_reward, float(self.total_reward) / self.episode)

        self.episode += 1
        self.num_step = 0
        self.episode_reward = 0

        logger.info("Episode %d starting...", self.episode)

        return self.obs2state(self.env.reset()[0])

    def close(self):

        if self.episode > 0:
            logger.info("Episode %d ended with reward %d after %d steps.",
                        self.episode, self.episode_reward, self.num_step)
            logger.info("Got %d total reward, with an average reward of %g per episode",
                        self.total_reward, float(self.total_reward) / self.episode)

        if self.env is not None:
            self.env.close()

    def obs2state(self, obs):

        state_dic = {}

        for (name, index) in zip(SCREEN_FEATURES._NAMES, SCREEN_FEATURES._INDEXS):
            state_dic[name] = obs.observation["screen"][index]
        for (name, index) in zip(MINIMAP_FEATURES._NAMES, MINIMAP_FEATURES._INDEXS):
            state_dic["mini_"+name] = obs.observation["minimap"][index]

        multi_select = obs.observation["multi_select"]
        state_dic["multi_select"] = self.multi2single(
            obs.observation["multi_select"])
        state_dic["build_queue"] = self.multi2single(
            obs.observation["build_queue"])

        available_actions = obs.observation["available_actions"]
        state_dic["available_actions"] = available_actions
        state_dic["available_actions_args_max"] = self.get_args_max(
            available_actions)

        other_names = ["player", "game_loop", "score_cumulative",
                       "single_select", "control_groups"]
        for name in other_names:
            state_dic[name] = obs.observation[name]

        useless_dict = {}
        useless_name = {"cargo", "cargo_slots_available",
                        "build_queue", "multi_select"}
        for name in useless_name:
            useless_dict[name] = obs.observation[name]

        return state_dic, useless_dict

    def get_args_max(self, available_actions):

        args_max_list = []

        for action_id in available_actions:
            arg_max_list = []
            for arg_name in ACTIONS._ARGS[action_id]:
                if arg_name == "screen" or arg_name == "screen2":
                    arg_max_list.append(self.screen_size)
                elif arg_name == "minimap":
                    arg_max_list.append(self.minimap_size)
                else:
                    arg_max_list.append(ACTIONS._ARGS_MAX[arg_name])
            args_max_list.append(arg_max_list)

        return args_max_list

    def multi2single(self, multi):

        single_list = [0 for i in range(7)]
        if multi.shape[0] > 0:
            id_list = []
            player_relative_list = []
            transport_list = []
            built_progress = 0.0
            single_num = 0.0
            for single in multi:
                id_list.append(single[0])
                player_relative_list.append(single[1])
                for i in range(2, 5):
                    single_list[i] += single[i]
                transport_list.append(single[5])
                single_num += 1
                built_progress += single[6]
            id_counts = np.bincount(id_list)
            player_relative_counts = np.bincount(player_relative_list)
            transport_counts = np.bincount(transport_list)
            single_list[0] = np.argmax(id_counts)
            single_list[1] = np.argmax(player_relative_counts)
            single_list[5] = np.argmax(transport_counts)
            single_list[6] = built_progress/single_num
        return single_list


if __name__ == "__main__":
    sc2 = SC2GameEnv(map_name="CollectMineralsAndGas")
    state, _ = sc2.reset()
    sc2.close()
