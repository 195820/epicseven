# -*- encoding=utf8 -*-
__author__ = "195820"

import sys 
sys.path.append(".")
sys.path.append("..")
from airtest.core.api import *
from location import Location

auto_setup(__file__,devices=["Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI"])

w,h=device().get_current_resolution()
dict={'w':(0.09*w,0.71*h),'s':(0.9*w,0.71*h),'e':(0.9*w,0.34*h),'n':(0.09*w,0.35*h),'map':(0.07*w,0.10*h),'confirm':(0.576*w,0.66*h),'camp':(0.11*w,0.93*h)}

#根据相对位点获取实际位点
def get_true_location(a):
    return (a[0]*w,a[1]*h)

def recover():
    touch(dict['camp'],duration=0.2)
    sleep(2)
    touch(dict['confirm'],duration=0.2)
    sleep(10)

    touch((0.30*w,0.54*h),duration=0.2)
    sleep(4)
    touch((0.73*w,0.56*h),duration=0.2)
    sleep(4)
    touch((0.73*w,0.36*h),duration=0.2)
    sleep(6)
    touch((0.73*w,0.36*h),duration=0.2)
    sleep(4)

    touch((0.68*w,0.56*h),duration=0.2)
    sleep(4)
    touch((0.73*w,0.56*h),duration=0.2)
    sleep(4)
    touch((0.73*w,0.36*h),duration=0.2)
    sleep(6)
    touch((0.73*w,0.36*h),duration=0.2)
    sleep(10)

def wsen(direction):
    for i in direction:
        touch(dict[i],times=2,duration=0.1)
        sleep(300)        

def mazen():
    touch(get_true_location(Location.random.value),times=2,duration=0.2)
    sleep(1)
    touch(get_true_location(Location.battle.value),times=2,duration=0.2)
    sleep(5)
    touch(get_true_location(Location.maze.value),times=2,duration=0.2)
    sleep(6)
    swipe((0.67*w,0.99*h),(0.67*w,0.01*h),duration=3)
    sleep(8)
    touch((0.64*w,0.84*h),duration=0.2)
    sleep(6)
    touch((0.84*w,0.92*h),duration=0.2)
    sleep(12)
    touch((0.04*w,0.54*h),duration=0.2)
    sleep(8)
    touch((0.84*w,0.92*h),duration=0.2)
    sleep(12)
    if not exists(Template(r"tpl1650014663425.png", record_pos=(0.284, 0.265), resolution=(1600, 900),rgb=True,threshold=0.5)):
        touch((0.88*w,0.043*h),duration=0.2)
        sleep(4)
    '''
    touch((0.84*w,0.92*h),times=2,duration=0.2)
    sleep(12)
    touch((0.87*w,0.03*h),duration=0.2)
    sleep(5)
    '''
    a=['w','s','n','w','w']
    wsen(a)
    
    #back home
    touch(dict['map'],duration=0.1)
    sleep(5)
    touch((0.62*w,0.005*h),duration=0.1)
    sleep(2)
    touch(dict['confirm'],duration=0.1)
    sleep(10)

    #recover emote
    recover()
    
    b=['e','s','e','s','e','s']
    wsen(b)
    
    #back home
    touch(dict['map'],duration=0.1)
    sleep(5)
    swipe((0.169*w,0.705*h),(0.486*w,0.708*h),duration=8)
    sleep(5)
    touch((0.184*w,0.606*h),duration=0.1)
    sleep(2)
    touch(dict['confirm'],duration=0.1)
    sleep(10)
    
    #back

if __name__ == '__main__':   
    mazen()