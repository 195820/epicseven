from enum import Enum

class Location(Enum):
    #界面唤醒
    random=(0.85,0.48)

    #竞技场
    arena=(0.67,0.90)
    #战斗按钮
    battle=(0.75,0.89)
    #战斗按钮：迷宫
    maze=(0.13,0.5)
    #战斗按钮：深渊
    abyss=(0.84,0.5)
    #战斗界面：自动战斗
    auto_battle=(0.87,0.04)
    #迷宫界面:w
    w=(0.09,0.71)
    #迷宫界面:s
    s=(0.9,0.71)
    #迷宫界面:e
    e=(0.9,0.34)
    #迷宫界面:n
    n=(0.09,0.35)
    #迷宫界面:露营
    camp=(0.11,0.93)
    #迷宫界面:地图
    map=(0.07,0.10)
    #迷宫界面:确认
    confirm=(0.576,0.66)
    #前往大厅
    hall=(0.89,0.95)
    #左上角返回
    return_on_leftup=(0.02,0.04)

    #支线故事(大厅)
    part_story=(0.85,0.89)
    #未记载的故事
    unremember_story=(0.66,0.53)
    #冒险
    adventure=(0.84,0.91)
    #开启宠物循环战斗
    auto_battle_normal=(0.45,0.77)
    #重复战斗结束的X
    end=(0.62,0.24)
    #确认
    confirm_normal=(0.91,0.92)
    #返回大厅
    return_on_rightdown=(0.20,0.91)

    #宠物
    pet=(0.33,0.90)

    #骑士团
    groups=(0.40,0.90)