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

def findkey(w,h):
    sleep(5)
    a=exists(Template(r"tpl1626254897369.png", record_pos=(-0.009, -0.068), resolution=(1600, 900),rgb=True))
    b=exists(Template(r"tpl1626256286052.png", record_pos=(-0.019, 0.001), resolution=(1600, 900),rgb=True))
    pos,times=get_random_arrays(20,10)  
    i=False
    # +next(pos) next(times)
    if a:
        sleep(2.5)
        touch((a[0]*2+next(pos),a[1]+40+next(pos)),duration=next(times))
        touch((a[0]*2+next(pos),a[1]+40+next(pos)),duration=next(times))
        sleep(2.5)
        touch((0.56*w+next(pos),0.70*h+next(pos)),duration=next(times))
        touch((0.56*w+next(pos),0.70*h+next(pos)),duration=next(times))
        i=True
        sleep(5)
    if b:
        sleep(2.5)
        touch((b[0]*2+next(pos),b[1]+40+next(pos)),duration=next(times))
        touch((b[0]*2+next(pos),b[1]+40+next(pos)),duration=next(times))
        sleep(2.5)
        touch((0.56*w+next(pos),0.70*h+next(pos)),duration=next(times))
        touch((0.56*w+next(pos),0.70*h+next(pos)),duration=next(times))
        i=True
        sleep(5)
    return i
  

def store(count):
    number,j,num=0,0,count
    w,h=device().get_current_resolution()
    i=random.randint(-10,10)
    touch((0.44*w+i,0.25*h-i),duration=0.12)
    sleep(0.5)
    touch((0.44*w-i,0.25*h+i),duration=0.18)
    sleep(5)
    while(count>=0):
        # +next(pos) +next(times)
        j+=1
        pos,times=get_random_arrays(24,20)
        key=findkey(w,h)
        swipe((0.68*w+next(pos),0.8*h+next(pos)),(0.68*w+next(pos),0.3*h+next(pos)),duration=1.5+next(times))
        sleep(4.0)
        key1=findkey(w,h)
        if key or key1:
            count-=1
            print('刷新次数:'+str(j)+'   获得书签:'+str(num-count))
            number=0
            sleep(2+next(times))
            touch((0.17*w+next(pos),0.9*h+next(pos)),duration=1+next(times))
            touch((0.17*w+next(pos),0.9*h+next(pos)),duration=1+next(times))
            sleep(2+next(times))
            touch((0.56*w+next(pos),0.62*h+next(pos)),duration=1+next(times))
            touch((0.56*w+next(pos),0.62*h+next(pos)),duration=1+next(times))
            sleep(2+next(times))
            continue
        print('刷新次数:'+str(j)+'   获得书签:'+str(num-count))
        number+=1
        if number>=100:
            print('太非了(100次没有书签)，已经自动停止')
            break
        sleep(2+next(times))
        touch((0.17*w+next(pos),0.9*h+next(pos)),duration=1+next(times))
        touch((0.17*w+next(pos),0.9*h+next(pos)),duration=1+next(times))
        sleep(1+next(times))
        touch((0.56*w+next(pos),0.62*h+next(pos)),duration=1+next(times))
        touch((0.56*w+next(pos),0.62*h+next(pos)),duration=1+next(times))
        sleep(2+next(times))
    print('刷新次数:'+str(j)+'   获得书签:'+str(num-count))

if __name__ == '__main__':
    store(int(sys.argv[1]))


