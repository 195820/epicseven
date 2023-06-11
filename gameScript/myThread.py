import threading 
import time
import ctypes 
from epicSeven.key.key import key1
from epicSeven.daily.daily import daily1
from epicSeven.expedition.expedition import expedition

class MyThread(threading.Thread):
    def __init__(self,func,list):
        threading.Thread.__init__(self)
        self.func = func
        self.list = list
        self.stop_flag = False

    def run(self):
        try:
            #list=[device,display_box]
            if self.func=="daily1":
                daily1(self.stop_flag,self.list)
            if self.func=="key1":
                key1(self.stop_flag,self.list)
            if self.func=="expedition1":
                daily1(self.stop_flag,self.list)
            self.stop_flag = True
        finally:
            print("ended")

    def stop(self):
        self.stop_flag = True

    def get_id(self): 
		# returns id of the respective thread 
        if hasattr(self, '_thread_id'): 
            return self._thread_id 
        for id, thread in threading._active.items(): 
            if thread is self: 
                return id

    def raise_exception(self): 
        thread_id = self.get_id() 
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 
            ctypes.py_object(SystemExit)) 
        if res > 1: 
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
            print('Exception raise failure') 

