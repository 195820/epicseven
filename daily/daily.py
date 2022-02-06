# -*- encoding=utf8 -*-
__author__ = "thl"

import sys
import random
from airtest.core.api import *

auto_setup(__file__,devices=["Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI"])

def get_random_arrays(num1,num2):
    random_array1=(random.randint(-15,15) for i in range(num1))
    random_array2=(random.uniform(0.15,0.5) for i in range(num2))
    return random_array1,random_array2

#增加任务完成的判定
def back_home():
    w,h=device().get_current_resolution()
    touch((0.98*w,0.04*h),times=2,duration=0.2)
    sleep(2)  
    touch((0.89*w,0.94*h),duration=0.2)
    sleep(15)

#竞技场
def arena():
    w,h=device().get_current_resolution()
    touch((0.8*w,0.7*h),times=2,duration=0.2)
    touch((0.48*w,0.03*h),times=2,duration=0.05)
    sleep(2)

    if not exists(Template(r"tpl1633875582935.png", record_pos=(-0.104, -0.005), resolution=(1600, 900))):
        touch((0.56*w,0.71*h),duration=0.2)
        sleep(2)
    else:
        touch((0.40*w,0.71*h),times=2,duration=0.2)
        sleep(2)
        
    touch((0.75*w,0.9*h),times=2,duration=0.5)
    sleep(2)
    touch((0.76*w,0.47*h),times=2,duration=0.2)
    sleep(10)
    touch((0.88*w,0.3*h),duration=0.2)
    a=1
    while(a):
        a=exists(Template(r"tpl1632998523422.png", record_pos=(0.228, 0.104), resolution=(1600, 900),rgb=True))
        if not a:
            #touch((0.58*w,0.66*h),times=2,duration=0.5)
            swipe((0.5*w,0.99*h),(0.5*w,0.01*h),duration=3)
            sleep(2)
            swipe((0.5*w,0.99*h),(0.5*w,0.01*h),duration=6)
            sleep(8)
            a=exists(Template(r"tpl1632998523422.png", record_pos=(0.228, 0.104), resolution=(1600, 900),rgb=True))
            if not a:
                break
        touch((a[0],a[1]),duration=0.2)
        sleep(18)
        touch((0.67*w,0.91*h),duration=0.2)
        sleep(30)
        touch((0.5*w,0.45*h),times=2,duration=0.1)
        sleep(10)
        touch((0.87*w,0.04*h),duration=0.1)
        sleep(90)
        touch((0.5*w,0.45*h),duration=0.1)
        sleep(20)
        touch((0.9*w,0.9*h),duration=0.1)
        sleep(20)
    back_home()
 
#深渊
def do_deep():
    w,h=device().get_current_resolution()
    touch((0.8*w,0.7*h),times=2,duration=0.2)
    touch((0.83*w,0.89*h),times=2,duration=0.2)
    sleep(5)
    touch((0.53*w,0.59*h),times=2,duration=0.2)
    sleep(6)
    touch((0.65*w,0.90*h),times=2,duration=0.2)
    sleep(10)
    touch((0.1*w,0.90*h),times=2,duration=0.2)
    touch((0.58*w,0.73*h),times=2,duration=0.2)
    sleep(8)
    touch((0.58*w,0.73*h),times=2,duration=0.2)
    sleep(8)
    back_home()
    
#迷宫商人   
def maze():
    w,h=device().get_current_resolution()

#获取水晶
def get_crystal():
    w,h=device().get_current_resolution()
    touch((0.19*w,0.27*h),duration=0.2)
    touch((0.19*w,0.27*h),duration=0.05)
    sleep(8)
    #满了
    touch((0.51*w,0.62*h),duration=0.05)
    sleep(6)
    touch((0.50*w,0.70*h),duration=0.05)
    back_home()

    
if __name__ == '__main__':        
    arena()
    do_deep()
    #maze()
    get_crystal()



