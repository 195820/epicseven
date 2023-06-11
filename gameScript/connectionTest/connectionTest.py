from airtest.core.api import *
import socket

class connectionTest():
    map={"夜神模拟器":62001,"蓝叠模拟器":5555,"网易mumu模拟器":7555,"雷电模拟器":5554}

    #正式连接返回设备号
    def connection(self,name,number,display_box):
        #port,只知道夜神的端口规律
        if name=="夜神模拟器":
            num=self.map[name] if number==1 else self.map[name]+22+number
        else:
            num=self.map[name]
        if self.check_port("localhost",num):
            device="Android://127.0.0.1:5037/127.0.0.1:"+str(num)+"?cap_method=JAVACAP&&ori_method=ADBORI"
            return device
        else:
            display_box.setText("连接失败")

    #连接测试
    def test(self,name,number,display_box):
        #port,只知道夜神的端口规律
        if name=="夜神模拟器":
            num=self.map[name] if number==1 else self.map[name]+22+number
        else:
            num=self.map[name]
        if self.check_port("localhost",num):
            device="Android://127.0.0.1:5037/127.0.0.1:"+str(num)+"?cap_method=JAVACAP&&ori_method=ADBORI"
            auto_setup(__file__, devices=[device])
            display_box.setText("连接成功")
        else:
            display_box.setText("连接失败")

    def check_port(self,host,port):
        s = socket.socket()
        try:
            s.connect((host, port))
            return True
        except:
            return False
        finally:
            s.close()
