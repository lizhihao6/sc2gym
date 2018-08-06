# from pysc2.lib import features, actions
# from define import ACTIONS

# _name_list = []
# _id_list = []
# _sizes_list = []

# _args_list = []
# args_dict = {}
# for _action_name in ACTIONS._NAMES:
#     _ArgumentTypes = actions.FUNCTIONS[_action_name].args
#     _args = []
#     for _ArgumentType in _ArgumentTypes:
#         _name = _ArgumentType.name
#         sizes = _ArgumentType.sizes
#         if _name not in _name_list:
#             args_dict[_name] = sizes
            
# print(args_dict)

from define import SCREEN_FEATURES,MINIMAP_FEATURES

for s in MINIMAP_FEATURES._SCALES:
    print(s)


#     # todo 封装args
#     args = [[numpy.random.randint(0, size) for size in arg.sizes]
#             for arg in self.action_spec.functions[function_id].args]

#                 actions.FUNCTIONS["no_op"]

#         obs_spec["feature_screen"] = (len(SCREEN_FEATURES),
#                                       aif.feature_dimensions.screen.y,
#                                       aif.feature_dimensions.screen.x)

#         obs_spec["feature_minimap"] = (len(MINIMAP_FEATURES),
#                                        aif.feature_dimensions.minimap.y,
#                                        aif.feature_dimensions.minimap.x)
# import numpy as np
# a = np.array([1,2,3,4,5,6,6])
# print(a[0])







#   @sw.decorate
#   def transform_action(self, obs, func_call, skip_available=False):
#     """Tranform an agent-style action to one that SC2 can consume.

#     Args:
#       obs: a `sc_pb.Observation` from the previous frame.
#       func_call: a `FunctionCall` to be turned into a `sc_pb.Action`.
#       skip_available: If True, assume the action is available. This should only
#           be used for testing or if you expect to make actions that weren't
#           valid at the last observation.

#     Returns:
#       a corresponding `sc_pb.Action`.

#     Raises:
#       ValueError: if the action doesn't pass validation.
#     """
#     func_id = func_call.function
#     try:
#       func = actions.FUNCTIONS[func_id]
#     except KeyError:
#       raise ValueError("Invalid function id: %s." % func_id)

#     # Available?
#     if not (skip_available or func_id in self.available_actions(obs)):
#       raise ValueError("Function %s/%s is currently not available" % (
#           func_id, func.name))

#     # Right number of args?
#     if len(func_call.arguments) != len(func.args):
#       raise ValueError(
#           "Wrong number of arguments for function: %s, got: %s" % (
#               func, func_call.arguments))

#     # Args are valid?
#     for t, arg in zip(func.args, func_call.arguments):
#       if t.name in ("screen", "screen2"):
#         sizes = self._screen_size_px
#       elif t.name == "minimap":
#         sizes = self._minimap_size_px
#       else:
#         sizes = t.sizes

#       if len(sizes) != len(arg):
#         raise ValueError(
#             "Wrong number of values for argument of %s, got: %s" % (
#                 func, func_call.arguments))

#       for s, a in zip(sizes, arg):
#         if not 0 <= a < s:
#           raise ValueError("Argument is out of range for %s, got: %s" % (
#               func, func_call.arguments))

#     # Convert them to python types.
#     kwargs = {type_.name: type_.fn(a)
#               for type_, a in zip(func.args, func_call.arguments)}

#     # Call the right callback to get an SC2 action proto.
#     sc2_action = sc_pb.Action()
#     kwargs["action"] = sc2_action
#     if func.ability_id:
#       kwargs["ability_id"] = func.ability_id
#     actions.FUNCTIONS[func_id].function_type(**kwargs)
#     return sc2_action










# class Features(object):
#   """Render feature layers from SC2 Observation protos into numpy arrays.

#   This has the implementation details of how to render a starcraft environment.
#   It translates between agent action/observation formats and starcraft
#   action/observation formats, which should not be seen by agent authors. The
#   starcraft protos contain more information than they should have access to.

#   This is outside of the environment so that it can also be used in other
#   contexts, eg a supervised dataset pipeline.
#   """

#   def __init__(self, game_info=None, screen_size_px=None, minimap_size_px=None,
#                hide_specific_actions=True):
#     """Initialize a Features instance.

#     Args:
#       game_info: A `sc_pb.ResponseGameInfo` from the game. Can be None if you
#           instead set `screen_size_px` and `minimap_size_px`.
#       screen_size_px: The screen resolution.
#       minimap_size_px: The minimap resolution.
#       hide_specific_actions: [bool] Some actions (eg cancel) have many
#           specific versions (cancel this building, cancel that spell) and can
#           be represented in a more general form. If a specific action is
#           available, the general will also be available. If you set
#           `hide_specific_actions` to False, the specific versions will also be
#           available, but if it's True, the specific ones will be hidden.
#           Similarly, when transforming back, a specific action will be returned
#           as the general action. This simplifies the action space, though can
#           lead to some actions in replays not being exactly representable using
#           only the general actions.

#     Raises:
#       ValueError: if game_info is None and screen or minimap sizes are missing.
#     """
#     if game_info:
#       fl_opts = game_info.options.feature_layer
#       screen_size_px = point.Point.build(fl_opts.resolution)
#       minimap_size_px = point.Point.build(fl_opts.minimap_resolution)
#     elif not (screen_size_px and minimap_size_px):
#       raise ValueError(
#           "Must provide either game_info or screen and minimap sizes")
#     self._screen_size_px = point.Point(*screen_size_px)
#     self._minimap_size_px = point.Point(*minimap_size_px)
#     self._hide_specific_actions = hide_specific_actions
#     self._valid_functions = self._init_valid_functions()
