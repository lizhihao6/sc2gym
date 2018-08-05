# SC2GYM

## 简介

SC2GYM意在简化PySC2 API的复杂调用，将PySC2封装成类似gym的环境，方便对算法的开发

**特别声明的是**：

1.部分代码参考了[islamelnabarawy/sc2gym](https://github.com/islamelnabarawy/sc2gym)

2.虽然封装成了类似gym的环境，但并未调用gym库，在部分调用上和gym可能存在一些区别，因此请仔细阅读本文档

3.测试环境基于windows10 + pysc2 version: 1.2

## 调用流程

```python
import sc2gym

env = sc2gym.SC2GameEnv(**kwargs)
state, _ = env.reset()
while(conditions):
    '''
        Your code is here.
    '''
    state, reward, done, _ = env.step()

env.close()
```

## 类型说明

### env
是对环境进行操作的基础类，封装有各种方法。

### state
返回类型是一个字典，其中参数有： 
```python
[
'''
feature layer 的 state
'''
"height_map", "visibility_map", "creep", "power", "player_id", "player_relative", "unit_type", "selected", "unit_hit_points", "unit_hit_points_ratio", "unit_energy", "unit_energy_ratio", "unit_shields", "unit_shields_ratio", "unit_density", "unit_density_aa", "effects",
''' 
minimap feature layer 的 state
'''
"mini_height_map", "mini_visibility_map", "mini_creep", "mini_camera", "mini_player_id", "mini_player_relative", "mini_selected","multi_select",
'''
其余state
'''
"build_queue",
"available_actions",
"available_actions_args_max",
"player", 
"game_loop", 
"score_cumulative",
"single_select", 
"control_groups"]
```
其中各个参数的大小及意义为:

### reward

### done

### useless_state

## 函数API

### sc2gym.SC2GameEnv()

**args**: 需要传入PySC2初始化所需的参数,例如传入mapname = "CollectMineralsAndGas"

**return**: env

**description**: 对环境的初始化


### sc2gym.SC2GameEnv.reset()

**args**: 需要传入PySC2初始化所需的参数,例如传入mapname = "CollectMineralsAndGas"

**return**: env

**description**: 对环境的初始化
