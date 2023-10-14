# -*- encoding=utf8 -*-
import sys
sys.path.append("..")
from ..location import Location
from airtest.core.api import *
import random
__author__ = "thl"

w,h=0,0

def daily1(stop_flag,list):
    auto_setup(__file__, devices=[list[0]])
    global w,h 
    comm=list[1]
    w,h = device().get_current_resolution()
    comm.update_signal.emit("执行中")
    arena()
    comm.update_signal.emit("竞技场完成")
    do_deep()
    comm.update_signal.emit("深渊完成")
    get_crystal()
    comm.update_signal.emit("圣域已领取")
    maze()
    comm.update_signal.emit("迷宫商人完成")
    pet()
    comm.update_signal.emit("每日宠物")
    groups()
    comm.update_signal.emit("团战讨伐完成")
    Adventure()
    comm.update_signal.emit("每日冒险完成"+"\n"+"每日全部完成")


# 根据相对位点获取实际位点


def get_true_location(a):
    return (a[0]*w, a[1]*h)

# 设置随机位点和时间


def get_random_arrays(num1, num2):
    random_array1 = (random.randint(-15, 15) for i in range(num1))
    random_array2 = (random.uniform(0.15, 0.5) for i in range(num2))
    return random_array1, random_array2

# 任务完成返回大厅


def back_home():
    touch((0.98*w, 0.04*h), times=2, duration=0.2)
    sleep(2)
    touch(get_true_location(Location.hall.value), duration=0.2)
    sleep(15)

# 竞技场


def arena():
    touch(get_true_location(Location.random.value), times=2, duration=0.2)
    touch((0.48*w, 0.03*h), times=2, duration=0.05)
    sleep(2)
    if not exists(Template(r"tpl1633875582935.png", record_pos=(-0.104, -0.005), resolution=(1600, 900))):
        touch((0.56*w, 0.71*h), times=2, duration=0.2)
        sleep(2)
    else:
        touch((0.40*w, 0.71*h), times=2, duration=0.2)
        sleep(2)

    touch(get_true_location(Location.arena.value), times=2, duration=0.5)
    sleep(2)
    touch((0.76*w, 0.47*h), times=2, duration=0.2)
    sleep(10)
    touch((0.88*w, 0.3*h), duration=0.2)
    a = 1
    sleep(10)
    while(a):
        a = exists(Template(r"tpl1652163610026.png", record_pos=(
            0.228, 0.104), resolution=(1600, 900), threshold=0.8))

        if not a:
            # touch((0.58*w,0.66*h),times=2,duration=0.5)
            swipe((0.5*w, 0.99*h), (0.5*w, 0.01*h), duration=3)
            sleep(2)
            swipe((0.5*w, 0.99*h), (0.5*w, 0.01*h), duration=6)
            sleep(8)
            a = exists(Template(r"tpl1652163610026.png", record_pos=(
                0.228, 0.104), resolution=(1600, 900), threshold=0.8))
            if not a:
                break
        touch((a[0], a[1]), duration=0.2)
        sleep(18)
        touch((0.67*w, 0.91*h), duration=0.2)
        sleep(30)
        touch((0.5*w, 0.45*h), times=2, duration=0.1)
        sleep(10)
        touch(get_true_location(Location.auto_battle.value), duration=0.1)
        sleep(50)
        touch((0.5*w, 0.45*h), duration=0.1)
        sleep(15)
        touch((0.9*w, 0.9*h), duration=0.1)
        sleep(20)
        
    back_home()

# 深渊


def do_deep():
    touch(get_true_location(Location.random.value), times=2, duration=0.2)
    sleep(1)
    touch(get_true_location(Location.battle.value), times=2, duration=0.2)
    sleep(5)
    touch((0.30*w, 0.92*h), times=2,duration=0.2)
    sleep(5)
    touch(get_true_location(Location.abyss.value), times=2, duration=0.2)
    sleep(6)
    touch((0.1*w, 0.90*h), times=2, duration=0.2)
    sleep(2)
    touch((0.58*w, 0.73*h), times=2, duration=0.2)
    sleep(8)
    touch((0.58*w, 0.73*h), times=2, duration=0.2)
    sleep(8)
    back_home()

# 迷宫商人


def maze():
    touch(get_true_location(Location.random.value), times=2, duration=0.2)
    sleep(1)
    touch(get_true_location(Location.battle.value), times=2, duration=0.2)
    sleep(5)
    touch((0.30*w, 0.92*h), times=2,duration=0.2)
    sleep(5)
    touch(get_true_location(Location.maze.value), times=2, duration=0.2)
    sleep(10)
    if(exists(Template(r"tpl1683703189357.png"))):
        a=exists(Template(r"tpl1683703189357.png"))
        touch((a[0], a[1]), duration=0.2)
    sleep(6)
    touch((0.63*w, 0.12*h), times=2,duration=0.2)
    sleep(6)
    touch((0.84*w, 0.92*h), duration=0.2)
    sleep(12)
    touch((0.84*w, 0.92*h), duration=0.2)

    touch((0.05*w, 0.5*h), times=80,duration=0.1)
    sleep(5)
    touch(get_true_location(Location.map.value), duration=0.2)
    sleep(5)
    swipe((0.544*w, 0.158*h), (0.544*w, 0.58*h), duration=6)
    sleep(5)
    touch((0.223*w, 0.153*h), duration=0.2)
    sleep(5)
    touch(get_true_location(Location.confirm.value), duration=0.2)
    sleep(10)
    if not exists(Template(r"tpl1650014663425.png", record_pos=(0.284, 0.265), resolution=(1600, 900),rgb=True,threshold=0.5)):
        touch(get_true_location(Location.auto_battle.value), duration=0.2)
        sleep(4)
    touch(get_true_location(Location.w.value), duration=0.2)
    sleep(65)
    touch((0.49*w, 0.48*h), times=2, duration=0.2)
    sleep(15)

    # 强化石、书签
    get_resources()
    swipe((0.68*w, 0.8*h), (0.68*w, 0.3*h), duration=6)
    sleep(4.0)
    get_resources()
    sleep(10)

    touch((0.02*w, 0.04*h), duration=0.2)
    sleep(5)

    touch((0.99*w, 0.04*h), duration=0.2)
    sleep(5)
    touch((0.5*w, 0.37*h), duration=0.2)
    sleep(5)
    touch((0.57*w, 0.60*h), duration=0.2)
    sleep(5)

    back_home()


# 获取强化石和书签
def get_resources():
    sleep(5)
    a = exists(Template(r"tpl1626256286052.png", record_pos=(-0.019,
               0.001), resolution=(1600, 900), rgb=True, threshold=0.6))
    b = exists(Template(r"tpl1650010999010.png", record_pos=(-0.019,
               0.001), resolution=(1600, 900), rgb=True, threshold=0.6))
    c = exists(Template(r"tpl1649837864428.png", record_pos=(-0.019,
               0.001), resolution=(1600, 900), rgb=True, threshold=0.6))

    D = find_all(Template(r"tpl1650012031334.png", record_pos=(-0.019,
                 0.001), resolution=(1600, 900), rgb=True, threshold=0.4))
    E = find_all(Template(r"tpl1650012844828.png", record_pos=(-0.019,
                 0.001), resolution=(1600, 900), rgb=True, threshold=0.4))
    F = find_all(Template(r"tpl1650012871493.png", record_pos=(-0.019,
                 0.001), resolution=(1600, 900), rgb=True, threshold=0.4))
    pos, times = get_random_arrays(100, 50)
    # +next(pos) next(times)
    # 解决重复问题，find_all函数
    if a:
        sleep(2.5)
        touch((a[0]*2+next(pos), a[1]+40+next(pos)), duration=next(times))
        touch((a[0]*2+next(pos), a[1]+40+next(pos)), duration=next(times))
        sleep(2.5)
        touch((0.56*w+next(pos), 0.70*h+next(pos)), duration=next(times))
        touch((0.56*w+next(pos), 0.70*h+next(pos)), duration=next(times))
        sleep(5)
    if b:
        sleep(2.5)
        touch((b[0]*2+next(pos), b[1]+40+next(pos)), duration=next(times))
        touch((b[0]*2+next(pos), b[1]+40+next(pos)), duration=next(times))
        sleep(2.5)
        touch((0.56*w+next(pos), 0.70*h+next(pos)), duration=next(times))
        touch((0.56*w+next(pos), 0.70*h+next(pos)), duration=next(times))
        sleep(5)
    if c:
        sleep(2.5)
        touch((c[0]*2+next(pos), c[1]+40+next(pos)), duration=next(times))
        touch((c[0]*2+next(pos), c[1]+40+next(pos)), duration=next(times))
        sleep(2.5)
        touch((0.56*w+next(pos), 0.70*h+next(pos)), duration=next(times))
        touch((0.56*w+next(pos), 0.70*h+next(pos)), duration=next(times))
        sleep(5)
    if D:
        for d in [x.get('result') for x in D]:
            sleep(2.5)
            touch((d[0]*2+next(pos), d[1]+40+next(pos)), duration=next(times))
            touch((d[0]*2+next(pos), d[1]+40+next(pos)), duration=next(times))
            sleep(2.5)
            touch((0.56*w+next(pos), 0.70*h+next(pos)), duration=next(times))
            touch((0.56*w+next(pos), 0.70*h+next(pos)), duration=next(times))
            sleep(5)
    if E:
        for e in [x.get('result') for x in E]:
            sleep(2.5)
            touch((e[0]*2+next(pos), e[1]+40+next(pos)), duration=next(times))
            touch((e[0]*2+next(pos), e[1]+40+next(pos)), duration=next(times))
            sleep(2.5)
            touch((0.56*w+next(pos), 0.70*h+next(pos)), duration=next(times))
            touch((0.56*w+next(pos), 0.70*h+next(pos)), duration=next(times))
            sleep(5)
    if F:
        for f in [x.get('result') for x in F]:
            sleep(2.5)
            touch((f[0]*2+next(pos), f[1]+40+next(pos)), duration=next(times))
            touch((f[0]*2+next(pos), f[1]+40+next(pos)), duration=next(times))
            sleep(2.5)
            touch((0.56*w+next(pos), 0.70*h+next(pos)), duration=next(times))
            touch((0.56*w+next(pos), 0.70*h+next(pos)), duration=next(times))
            sleep(5)
# 获取水晶


def get_crystal():
    touch(get_true_location(Location.random.value), times=2, duration=0.2)
    sleep(2)
    touch((0.19*w, 0.27*h), times=2, duration=0.2)
    sleep(5)
    a = exists(Template(r"tpl1649839339328.png",
               record_pos=(-0.003, 0.111), resolution=(1600, 900)))
    if a:
        touch((a[0], a[1]), times=2, duration=0.2)
        sleep(10)
        touch((0.8*w, 0.8*h), times=2, duration=0.2)
        sleep(5)
    else:
        touch((0.51*w, 0.45*h), times=2, duration=0.2)
        sleep(5)
        touch((0.82*w, 0.91*h), times=2, duration=0.2)
        sleep(5)
        touch((0.63*w, 0.66*h), times=2, duration=0.2)
        sleep(10)
        touch(get_true_location(Location.return_on_leftup.value),
              times=2, duration=0.2)
        sleep(5)
    forest()
    back_home()


def forest():
    touch((0.26*w, 0.23*h), times=2, duration=0.2)
    sleep(5)
    # 萝卜
    touch((0.59*w, 0.61*h), times=2, duration=0.2)
    sleep(5)
    touch((0.05*w, 0.78*h), times=2, duration=0.2)
    sleep(3)
    # 企鹅
    touch((0.43*w, 0.19*h), times=2, duration=0.2)
    sleep(5)
    touch((0.31*w, 0.71*h), times=2, duration=0.2)
    sleep(3)
    # 狗粮
    touch((0.78*w, 0.36*h), times=2, duration=0.2)
    sleep(5)
    touch((0.31*w, 0.71*h), times=2, duration=0.2)
    sleep(3)

#宠物
def pet():
    touch(get_true_location(Location.random.value), times=2, duration=0.2)
    sleep(1)
    touch(get_true_location(Location.pet.value), times=2, duration=0.1)
    sleep(2)
    #领养
    touch((0.69*w, 0.90*h), times=2, duration=0.2)
    sleep(3)
    touch((0.42*w, 0.83*h), times=1, duration=0.2)
    sleep(10)
    touch((0.47*w, 0.90*h), times=1, duration=0.2)
    sleep(3)
    touch((0.50*w, 0.95*h), times=1, duration=0.2)
    sleep(3)
    back_home()



#团本每日
#按照每天先打团计算
def groups():
    touch(get_true_location(Location.random.value), times=2, duration=0.2)
    sleep(1)
    touch(get_true_location(Location.groups.value), times=2, duration=0.1)
    sleep(8)

    touch((0.51*w, 0.73*h), times=2, duration=0.2)
    sleep(3)

    #世界首领
    touch((0.88*w, 0.29*h), times=1, duration=0.2)
    sleep(3)
    a=exists(Template(r"tpl1686482674338.png", record_pos=(-0.198, 0.051), resolution=(1920, 1080),threshold=0.85))
    touch((a[0]*w,a[1]*h), times=1, duration=0.2)
    sleep(3)
    #领取队伍使用奖励
    touch((0.55*w, 0.76*h), times=1, duration=0.2)
    sleep(3)
    for i in range(2):
        touch((0.72*w, 0.91*h), times=1, duration=0.2)
        sleep(3)
        touch((0.79*w, 0.83*h), times=1, duration=0.2)
        sleep(3)
        touch((0.85*w, 0.90*h), times=1, duration=0.2)
        sleep(3)
        touch((0.13*w, 0.91*h), times=1, duration=0.2)
        sleep(3)
        touch((0.67*w, 0.91*h), times=1, duration=0.2)
        sleep(150)
        touch((0.51*w, 0.86*h), times=1, duration=0.2)
        sleep(3)
        touch((0.51*w, 0.86*h), times=1, duration=0.2)
        sleep(3)
        touch((0.91*w, 0.91*h), times=1, duration=0.2)
        sleep(8)
    touch((0.03*w, 0.04*h), times=1, duration=0.2)
    sleep(3)
    touch((0.51*w, 0.73*h), times=2, duration=0.2)
    sleep(3)
    #每日捐赠
    touch((0.87*w, 0.57*h), times=1, duration=0.2)
    sleep(3)
    touch((0.68*w, 0.60*h), times=1, duration=0.2)
    sleep(3)
    touch((0.49*w, 0.74*h), times=1, duration=0.2)
    sleep(3)
    touch((0.68*w, 0.91*h), times=1, duration=0.2)
    sleep(3)
    touch((0.49*w, 0.74*h), times=1, duration=0.2)
    sleep(3)
    back_home()


#进行冒险每日
def Adventure():
    touch(get_true_location(Location.random.value), times=2, duration=0.2)
    sleep(1)
    touch(get_true_location(Location.part_story.value), times=2, duration=0.1)
    sleep(2)
    touch(get_true_location(Location.unremember_story.value), times=2, duration=0.1)
    sleep(5)
    touch(get_true_location(Location.adventure.value), times=2, duration=0.1)
    sleep(8)
    #三个战斗按钮
    touch((0.81*w, 0.92*h), times=1, duration=0.2)
    sleep(8)
    touch((0.81*w, 0.92*h), times=1, duration=0.2)
    sleep(8)

    if(not exists(Template(r"tpl1686474215870.png", record_pos=(-0.013, 0.156), resolution=(1920, 1080),threshold=0.85))):
        touch(get_true_location(Location.auto_battle_normal.value), times=1, duration=0.1)
        sleep(3)
    touch((0.81*w, 0.92*h), times=1, duration=0.2)
    sleep(2)

    #进行重复战斗一次一分钟
    sleep(2000)

    touch(get_true_location(Location.end.value), times=1, duration=0.1)
    sleep(2)
    touch(get_true_location(Location.random.value), times=1, duration=0.1)
    sleep(2)
    touch((0.42*w, 0.72*h), times=2, duration=0.2)
    sleep(2)
    touch(get_true_location(Location.confirm_normal.value), times=1, duration=0.1)
    sleep(2)
    touch(get_true_location(Location.return_on_rightdown.value), times=1, duration=0.1)
    sleep(8)



