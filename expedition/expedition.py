# -*- encoding=utf8 -*-
__author__ = "thl"
'''初次执行的特殊操作未实现'''

from airtest.core.api import *
import random
import sys

auto_setup(__file__,devices=["Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI"])
battleflag=0

def get_random_arrays(num1,num2):
    random_array1=(random.randint(-15,15) for i in range(num1))
    random_array2=(random.uniform(0.15,0.5) for i in range(num2))
    return random_array1,random_array2

def do_wanted(w,h):
    autoflag=0
    global battleflag
    while(True):
        a=exists(Template(r"tpl1627784392811.png", record_pos=(0.426, -0.081), resolution=(1600, 900)))
        i=random.randint(-10,10)
        if a:
            touch((0.92*w+i,0.44*h-i),duration=0.1)
            sleep(4)
            touch((0.87*w+i,0.92*h-i),duration=0.5)
            sleep(15)
            touch((0.87*w+i,0.92*h-i),duration=0.3)
            sleep(5)
            if battleflag==0:
                touch((0.63*w+i,0.69*h-i),duration=0.3)
                battleflag=1
                sleep(10)
            if autoflag==0:
                if not exists(Template(r"tpl1650014663425.png", record_pos=(0.284, 0.265), resolution=(1600, 900),rgb=True,threshold=0.5)):
                    touch((0.88*w,0.043*h),duration=0.2)
                    autoflag=1
                    sleep(8)
            sleep(400)
            touch((0.12*w+i,0.92*h-i),duration=0.3)
            sleep(8)
            continue
        touch((0.38*w+i,0.53*h-i),duration=0.3)
        sleep(4)
        break
    
def expedition(a,b,c):
    i=random.randint(-10,10)
    w,h=device().get_current_resolution()
    touch((0.38*w+i,0.16*h-i),times=2,duration=1)
    touch((0.38*w+i,0.16*h-i),times=2,duration=1)
    sleep(5)
    touch((0.56*w+i,0.46*h-i),duration=1)
    sleep(3)
    while(True):
        
        #左上
        if a==1:
            touch((0.34*w+i,0.33*h-i),duration=1)
            sleep(3)
            do_wanted(w,h)
        
        #右上
        if b==1:
            touch((0.72*w-i,0.33*h-i),duration=1)
            sleep(3)
            do_wanted(w,h)
        
        #下
        if c==1:
            touch((0.62*w+i,0.74*h-i),duration=1)
            sleep(3)
            do_wanted(w,h)

        sleep(1200)
if __name__ == '__main__':
    flag=[False,False,False]
    expedition(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))