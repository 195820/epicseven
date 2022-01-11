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

def nine_four(num):
    w,h=device().get_current_resolution()
    dict={'w':(0.09*w,0.71*h),'s':(0.9*w,0.71*h),'e':(0.9*w,0.34*h),'n':(0.09*w,0.35*h)}
    while(num>0):
        touch((0.81*w,0.91*h),duration=0.2)
        sleep(8)
        touch((0.81*w,0.91*h),duration=0.2)
        sleep(5)
        touch((0.81*w,0.91*h),duration=0.2)
        sleep(30)
        touch(dict['s'],duration=0.5)
        sleep(30)
        touch(dict['w'],duration=0.5)
        sleep(30)
        touch(dict['s'],duration=0.5)
        sleep(30)
        touch(dict['w'],duration=0.5)
        sleep(60)
        
        touch((0.08*w,0.10*h),duration=0.2)
        sleep(2)
        swipe((0.49*w,0.393*h),(0.313*w,0.699*h),duration=8)
        touch((0.444*w,0.118*h),duration=0.2)
        sleep(2)
        touch((0.57*w,0.66*h),duration=0.2)
        sleep(40)   
        
        touch(dict['w'],duration=0.5)
        sleep(30)
        touch(dict['n'],duration=0.5)
        sleep(40)
        
        touch((0.08*w,0.10*h),duration=0.2)
        sleep(3)
        touch((0.55*w,0.40*h),duration=0.2)
        sleep(3)
        touch((0.57*w,0.66*h),duration=0.2)
        sleep(3)
        touch((0.50*w,0.55*h),duration=0.2)
        sleep(4)
        touch((0.57*w,0.66*h),duration=0.2)
        sleep(6)
        touch((0.57*w,0.66*h),duration=0.2)
        sleep(6)
        touch((0.9*w,0.9*h),times=2,duration=0.2)
        sleep(10)
        num-=1
        if(num%20==0):
            clear_weapon()
            #clear_heros()

def clear_weapon():
    w,h=device().get_current_resolution()
    touch((0.83*w,0.05*h),duration=0.2)
    sleep(5)
    touch((0.45*w,0.14*h),duration=0.2)
    sleep(5)
    touch((0.14*w,0.22*h),duration=0.2)
    sleep(5)
    touch((0.85*w,0.22*h),duration=0.2)
    sleep(5)
    touch((0.14*w,0.22*h),duration=0.2)
    sleep(5)
    touch((0.83*w,0.73*h),duration=0.2)
    sleep(5)
    touch((0.30*w,0.22*h),duration=0.2)
    sleep(5)
    touch((0.57*w,0.72*h),duration=0.2)
    sleep(8)
    touch((0.07*w,0.22*h),duration=0.2)
    sleep(5)
    
def clear_heros():
    w,h=device().get_current_resolution()
    touch((0.97*w,0.05*h),duration=0.2)
    sleep(5)
    touch((0.87*w,0.94*h),duration=0.2)
    sleep(5)
    touch((0.11*w,0.91*h),times=2,duration=0.2)
    sleep(5)
    touch((0.11*w,0.39*h),duration=0.2)
    sleep(5)
    touch((0.82*w,0.12*h),duration=0.2)
    sleep(5)
    touch((0.53*w,0.57*h),duration=0.2)
    sleep(5)
    touch((0.22*w,0.86*h),duration=0.2)
    sleep(5)
    while(exists(Template(r"tpl1636790342305.png", record_pos=(0.343, -0.049), resolution=(1600, 900)))):
          touch((0.87*w,0.39*h),times=12,duration=0.1)
          sleep(2)
          touch((0.62*w,0.91*h),duration=0.2)
          sleep(2)
          touch((0.58*w,0.60*h),duration=0.2)
          sleep(4)
          touch((0.45*w,0.72*h),duration=0.2)
          sleep(2)
    touch((0.97*w,0.05*h),duration=0.2)
    sleep(5)
    touch((0.95*w,0.76*h),duration=0.2)
    sleep(15)    
    
if __name__ == '__main__':
    nine_four(int(sys.argv[1]))