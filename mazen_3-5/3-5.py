# -*- encoding=utf8 -*-
__author__ = "195820"

from airtest.core.api import *

auto_setup(__file__,devices=["Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI"])

w,h=device().get_current_resolution()
dict={'w':(0.09*w,0.71*h),'s':(0.9*w,0.71*h),'e':(0.9*w,0.34*h),'n':(0.09*w,0.35*h),'map':(0.07*w,0.10*h),'confirm':(0.576*w,0.66*h),'camp':(0.11*w,0.93*h),'auto':(0.88*w,0.043*h),'s1':(0.80*w,0.91*h),'s2':(0.88*w,0.91*h),'s3':(0.94*w,0.91*h)}


def wsen(direction):
    for i in direction:
        touch(dict[i],times=2,duration=0.1)
        sleep(300)   

def battle():
    pass
        
def mazen():
    #进入迷宫
    touch((0.8*w,0.7*h),times=2,duration=0.2)
    touch((0.83*w,0.89*h),times=2,duration=0.2)
    sleep(5)
    touch((0.9*w,0.28*h),times=2,duration=0.2)
    sleep(5)
    touch((0.65*w,0.88*h),times=2,duration=0.2)
    sleep(5)
    swipe((0.67*w,0.99*h),(0.67*w,0.01*h),duration=3)
    sleep(8)
    touch((0.84*w,0.92*h),duration=0.2)
    sleep(12)
    touch((0.05*w,0.62*h),duration=0.2)
    sleep(6)
    touch((0.84*w,0.92*h),duration=0.2)
    sleep(3)
    touch((0.03*w,0.53*h),times=70,duration=0.1)
    if(exists(Template(r"tpl1653380123643.png", record_pos=(0.374, 0.236), resolution=(1600, 900)))):
        touch(dict['auto'],duration=0.2)
    sleep(2)
    #上buff
    touch(dict['map'],duration=0.1)
    sleep(4)
    swipe((0.169*w,0.158*h),(0.395*w,0.655*h),duration=8)
    sleep(5)
    touch((0.167*w,0.284*h),duration=0.1)
    sleep(2)
    touch(dict['confirm'],duration=0.1)
    sleep(10)
    touch(dict['n'],duration=0.1)
    sleep(8)
    touch((0.53*w,0.57*h),times=2,duration=0.2)
    #手动战斗
    
    #消耗心情
    for i in range(14):
        touch(dict['map'],duration=0.1)
        sleep(4)
        touch((0.50*w,0.47*h),duration=0.1)
        sleep(2)
        touch(dict['confirm'],duration=0.1)
        sleep(4)
        touch(dict['map'],duration=0.1)
        sleep(4)
        touch((0.19*w,0.40*h),duration=0.1)
        sleep(2)
        touch(dict['confirm'],duration=0.1)
        sleep(4)
    #续buff
    #走迷宫

if __name__ == '__main__':   
    #一票木龙
    