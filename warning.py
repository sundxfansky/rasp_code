#!/usr/bin/python3
#coding=utf-8
#author：sundxfansky@sjtu.edu.cn


import time 
import threading
def fun_timer():
      print('Hello Timer!')
timer = threading.Timer(5, fun_timer)
print()
timer.start()
print("start....")
for i in range(4):
    time.sleep(1)
    print(str(5 - i) + '.......')