# -*- encoding=utf8 -*-
__author__ = "thl"

import sys
import random
from airtest.core.api import *

auto_setup(__file__,devices=["Android://127.0.0.1:5037/127.0.0.1:62001?cap_method=JAVACAP&&ori_method=ADBORI"])
w,h=device().get_current_resolution()

def buff(x):
    while(True):
        #进入讨伐界面
        #获取一个循环的体力，ocr leaf<=8 break
        #执行讨伐
        #返回大厅

if __name__=='__main__':
    #0是讨伐 1是符文 2是贡献度 
    buff(int(sys.argv[1]))