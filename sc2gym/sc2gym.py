import logging
from define import SCREEN_FEATURES, MINIMAP_FEATURES, ACTIONS

import gym
from pysc2.env import sc2_env
from pysc2.env.environment import StepType
from pysc2.lib import actions

__author__ = 'lizhihao6'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class SC2GameEnv(gym.Env):

    metadata = {'render.modes': [None, 'human']}

    def __init__(self, **kwargs) -> None:

        super().__init__()
        self._kwargs = kwargs
        self._env = None
        self._episode = 0
        self._num_step = 0
        self._episode_reward = 0
        self._total_reward = 0

    def step(self, action):

        self._num_step += 1

        if action[0] not in self.available_actions:
            logger.warning("Attempted unavailable action: %s", action)
            action = [0]

        try:
            obs = self._env.step(
                [actions.FunctionCall(action[0], action[1:])])[0]
        except KeyboardInterrupt:
            logger.info("Interrupted. Quitting...")
            return None, 0, True, {}
        except Exception:
            logger.exception(
                "An unexpected error occurred while applying action to environment.")
            return None, 0, True, {}

        self.available_actions = obs.observation['available_actions']
        reward = obs.reward
        self._episode_reward += reward
        self._total_reward += reward
        # todo: obs to numpy
        return obs, reward, obs.step_type == StepType.LAST, {}

    # 每训练到一定episode终止训练，一次训练由多个episode构成
    def reset(self):

        if self._env is None:
            self._env = sc2_env.SC2Env(**self._kwargs)

        if self._episode > 0:
            logger.info("Episode %d ended with reward %d after %d steps.",
                        self._episode, self._episode_reward, self._num_step)
            logger.info("Got %d total reward so far, with an average reward of %g per episode",
                        self._total_reward, float(self._total_reward) / self._episode)

        self._episode += 1
        self._num_step = 0
        self._episode_reward = 0

        logger.info("Episode %d starting...", self._episode)
        obs = self._env.reset()[0]

        self.available_actions = obs.observation['available_actions']

        # todo: obs2numpy
        return obs

    def save_replay(self, replay_dir): -> None
        self._env.save_replay(replay_dir)
        
    def _close(self): -> None

        if self._episode > 0:
            logger.info("Episode %d ended with reward %d after %d steps.",
                        self._episode, self._episode_reward, self._num_step)
            logger.info("Got %d total reward, with an average reward of %g per episode",
                        self._total_reward, float(self._total_reward) / self._episode)

        if self._env is not None:
            self._env.close()

        super()._close()