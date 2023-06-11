# -*- encoding=utf8 -*-
__author__ = "thl"
'''初次执行的特殊操作未实现'''

from airtest.core.api import *
from airtest.aircv import *
import random
import sys
sys.path.append('..')

def expedition():
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
        screen = G.DEVICE.snapshot() 
        # 局部截图
        local_screen = aircv.crop_image(screen,(714,129,795,157))

        # 将我们的目标截图设置为一个Template对象
        tempalte = Template(r"tpl1656226095461.png")
        # 在局部截图里面查找指定的图片对象
        pos = tempalte.match_in(local_screen)

        i=random.randint(-10,10)
        if not (pos):
            touch((0.71*w+i,0.23*h-i),duration=0.1)
            sleep(4)
            touch((0.92*w+i,0.73*h-i),duration=0.1)
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
            sleep(500)
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

        break
if __name__ == '__main__':
    expedition(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))







