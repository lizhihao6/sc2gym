# SC2GYM

## 简介

SC2GYM意在简化PySC2 API的复杂调用, 将PySC2封装成类似gym的环境, 方便对算法的开发

**特别声明的是**：

1.部分代码参考了[islamelnabarawy/sc2gym](https://github.com/islamelnabarawy/sc2gym)

2.虽然封装成了类似gym的环境, 但并未调用gym库, 在部分调用上和gym可能存在一些区别, 因此请仔细阅读本文档

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
    state, reward, done, _ = env.step(action)

env.close()
```

## 类型说明

### env
是对环境进行操作的基础类, 封装有各种方法

### state
返回类型是一个字典, 其中参数有： 
```python
[
# feature layer 的 state
"height_map", "visibility_map", "creep", "power", "player_id", "player_relative", "unit_type", "selected", "unit_hit_points", "unit_hit_points_ratio", "unit_energy", "unit_energy_ratio", "unit_shields", "unit_shields_ratio", "unit_density", "unit_density_aa", "effects",
 
# minimap feature layer 的 state
"mini_height_map", "mini_visibility_map", "mini_creep", "mini_camera", "mini_player_id", "mini_player_relative", "mini_selected",

# 其余state
"multi_select",
"build_queue",
"available_actions",
"available_actions_args_max",
"player", 
"game_loop", 
"score_cumulative",
"single_select", 
"control_groups"
]
```
其中各个参数的大小及意义为:

| 参数名 | sizes | max_value | 描述 |
| ------------ | :------------: | :------------: | ------------ |
| height_map | (screen_size, screen_size) | 256 | 地形高度 |
| visibility_map | (screen_size, screen_size) | 3 | 地图的可见性 [隐藏, 可见, 暂时可见, ？] |
| creep | (screen_size, screen_size) | 1 | 是否有虫族菌层覆盖 |
| power | (screen_size, screen_size) | 1 | 是否有神族水晶塔(只显示己方水晶塔) |
| player_id | (screen_size, screen_size) | 16 | 谁拥有当前单位, id是唯一确定的 |
| player_relative | (screen_size, screen_size) | 4 | 当前单位和己方的关系  [背景, 己方, 盟友, 中立, 敌方]  |
| unit_type | (screen_size, screen_size) | 1850 | 当前单位的类型, 详见[pysc2/lib/units.py](https://github.com/deepmind/pysc2/blob/master/pysc2/lib/units.py) |
| selected | (screen_size, screen_size) | 1 | 当前单位是否被选中 |
| unit_hit_points | (screen_size, screen_size) | 1600 | 当前单位的生命值是多少 |
| unit_hit_points_ratio | (screen_size, screen_size) | 256 | 当前单位的生命恢复速率 |
| unit_energy | (screen_size, screen_size) | 1000 | 当前单位的能量值 |
| unit_energy_ratio | (screen_size, screen_size) | 256 | 当前单位的能量恢复速率 |
| unit_shields | (screen_size, screen_size) | 1000 | 当前单位的护盾值 |
| unit_shields_ratio | (screen_size, screen_size) | 256 | 当前单位的护盾恢复速率 |
| unit_density | (screen_size, screen_size) | 16 | 当前像素有多少单位 |
| unit_density_aa | (screen_size, screen_size) | 256 | 当前像素上的单位, 总共覆盖了该像素的多少面积 |
| effects | (screen_size, screen_size) | 16 | 当前单位的模式切换, 科技升级 |
| mini_height_map | (minimap_size, minimap_size) | 256 | 小地图地形高度 |
| mini_visibility_map | (minimap_size, minimap_size) | 3 | 小地图的可见性 [隐藏, 可见, 暂时可见, ？] |
| mini_creep | (minimap_size, minimap_size) | 1 | 小地图是否有虫族菌层覆盖 |
| mini_camera | (minimap_size, minimap_size) | 1 | 当前部分在大地图是否可见 |
| mini_player_id | (minimap_size, minimap_size) | 17 | 小地图上谁拥有当前单位, id是唯一确定的 |
| mini_player_relative | (minimap_size, minimap_size) | 4 | 小地图上当前单位和己方的关系  [背景, 己方, 盟友, 中立, 敌方] |
| mini_selected | (minimap_size, minimap_size) | 1 | 小地图上当前单位是否被选中 |
| multi_select | (7) | [1850, 3, 1600, 1000, 1000, 1, 100] | [选中单位出现最多的单位的类型[pysc2/lib/units.py](https://github.com/deepmind/pysc2/blob/master/pysc2/lib/units.py), 选中单位和己方的关系的众数, 选中单位的总计生命值, 选中单位的总计护盾值, 选中单位的总计能量值, 选中单位是否被运送的众数, 选中单位的平均建造进度 ] |
| build_queue | (7) | [1850, 3, 1600, 1000, 1000, 1, 100] | 与multi_select相同, 但是全部单位为全部正在监造的单位 |
| available_actions | (n) | [514, 514 ...] | 下一步可进行的动作的id |
| available_actions_args_max | (n, args_n) | [  [ [p], [x, y] ] , ...  ] | 下一步的可执行的动作的所需的参数的列表, 长度与available_actions相同, 比如取available_actions_args_max[0] 代表得到available_actions[0]所需的参数列表, 其形式为 [ [args_0], [args_1], ... ] 其中[args_0] 代表所需的第一个参数的最大值, 可能为离散状态, 这时args_0为总共有多少种状态, 也可能代表屏幕上的一个点, 这时候[args_0]为[max_x,max_y]即屏幕上x,y能取到的最大的点 |
| player | (11) | unknown | 给定player的相关信息 [player_id, 矿物储量, 气储量, 当前人口, 人口上限, 战斗人口, 农民人口, 空闲农民数, 军队数量(这里跟人口不一样, 因为例如神族一个龙骑占2人口), P的传送门数量, Z的幼虫数量] |
| game_loop | (1) | unknown | unknown | 
| score_cumulative | (13) | unknown | 累计分数 [idle_production_time, idle_worker_time, total_value_units, total_value_structures, killed_value_units, killed_value_structures, collected_minerals, collected_vespene, collection_rate_minerals, collection_rate_vespene, spent_minerals, spent_vespene]  |
| single_select | (7) | [1850, 3, 1600, 1000, 1000, 1, 100] | [选中单位的类型[pysc2/lib/units.py](https://github.com/deepmind/pysc2/blob/master/pysc2/lib/units.py), 选中单位和己方的关系, 选中单位的生命值, 选中单位的护盾值, 选中单位的能量值, 选中单位是否被运送, 选中单位的建造进度 ] |
| control_groups | (10, 2)| [1850, n] | 编组, 2维含义分别是leader_unit_type和单位数量 |

### reward
返回PySC2默认的reward
### done
返回PySC2默认的是否结束
### useless state
返回类型是一个字典, 其中参数有：
```python
["cargo", "cargo_slots_available", "build_queue", "multi_select"]
```
这里的build_queue以及multi_select均为官方默认, 维度可变不容易处理


### useless_state

## 函数API

### sc2gym.SC2GameEnv(**kwargs)

**args**: **kwargs: 需要传入PySC2初始化所需的参数,例如传入 mapname = "CollectMineralsAndGas"

**return**: env

**description**: 对环境的初始化


### sc2gym.SC2GameEnv.reset()

**args**: None

**return**: state, useless_state

**description**: 重置环境

### sc2gym.SC2GameEnv.step(action)

**args**: action: 传入一个列表, 第一项为action_id, 之后为这个action的各个args [action_id, [args_0], [args_1] ... ]

**return**: state, reward, done, useless_state

**description**: 进行一步action

### sc2gym.SC2GameEnv.close()

**args**: None

**return**: None

**description**: 关闭环境