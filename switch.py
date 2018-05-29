#!/usr/bin/python3
#coding=utf-8
#author：sundxfansky@sjtu.edu.cn

#继电器模块驱动 2_raly_model drive
# #测试程序
# GPIO.setmode(GPIO.BOARD)
# #给定初始值
# GPIO.setup(36, GPIO.OUT, initial = GPIO.LOW)
# GPIO.setup(38, GPIO.OUT, initial = GPIO.LOW)
# time.sleep(2)
# print("opening....")
# GPIO.output(36,GPIO.HIGH)
# GPIO.output(38,GPIO.HIGH)
# time.sleep(10)
# GPIO.cleanup()

#初始化开关
def switch_init(switch1 = 36,switch2 = 38):
    print("Switch initializing......")
    gpio.setup(switch1, gpio.OUT, initial = gpio.LOW)
    gpio.setup(switch2, gpio.OUT, initial = gpio.LOW)
    print("Switch initialized")

#开启驱动版
def open_drive_board(switch = 36):
    print("Opening drive board......")
    gpio.output(switch,gpio.HIGH)
    print("Opened drive board")

#向前走
def change_move_forward(switch = 38):
    print("Changing move forward.....")
    gpio.output(switch,gpio.HIGH)
    print("changed move forward")

#向后走
def change_move_back(switch = 38):
    print("Changing move back.....")
    gpio.output(switch,gpio.LOW)
    print("changed move back")
