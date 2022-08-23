# -*- encoding=utf8 -*-
from location import Location
from airtest.core.api import *
import random
__author__ = "thl"

import sys
sys.path.append("..")
sys.path.append(".")

auto_setup(__file__, devices=[
           "Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI"])
w, h = device().get_current_resolution()

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
    touch(get_true_location(Location.maze.value), times=2, duration=0.2)
    sleep(10)
    touch((0.64*w, 0.32*h), duration=0.2)
    sleep(6)
    touch((0.84*w, 0.92*h), duration=0.2)
    sleep(12)
    touch((0.84*w, 0.92*h), duration=0.2)
    sleep(12)

    touch(get_true_location(Location.map.value), duration=0.2)
    sleep(5)
    swipe((0.544*w, 0.158*h), (0.544*w, 0.58*h), duration=6)
    sleep(5)
    touch((0.223*w, 0.153*h), duration=0.2)
    sleep(5)
    touch(get_true_location(Location.confirm.value), duration=0.2)
    sleep(10)
    touch(get_true_location(Location.auto_battle.value), duration=0.2)
    sleep(4)
    touch(get_true_location(Location.w.value), duration=0.2)
    sleep(25)
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


if __name__ == '__main__':
    arena()
    do_deep()
    get_crystal()
    maze()
