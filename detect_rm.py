import RPi.GPIO as gpio
import time, sys

gpio.setmode(gpio.BOARD)
sc_motor_a = 7
sc_motor_b = 16

gpio.setup(sc_motor_a, gpio.IN, pull_up_down = gpio.PUD_UP)   #读取左轮脉冲数据,加入上拉电阻保护
gpio.setup(sc_motor_b, gpio.IN, pull_up_down = gpio.PUD_UP)   #读取右轮脉冲数据，加入上拉电阻保护
counter_sc_motor_a = 0      #左轮脉冲初值
counter_sc_motor_b = 0     #右轮脉冲初值
def get_motor_a_rpm(channel):          #边缘检测回调函数
    global counter_sc_motor_a                 #设置为全局变量
    if gpio.event_detected(sc_motor_a):        #检测到一个脉冲则脉冲数加1
        counter_sc_motor_a = counter_sc_motor_a + 1
        print(counter)
def get_motor_a_rpm(channel):          #边缘检测回调函数
    global counter_sc_motor_a                 #设置为全局变量
    if gpio.event_detected(sc_motor_a):        #检测到一个脉冲则脉冲数加1
        counter_sc_motor_a = counter_sc_motor_a + 1
        print(counter)
#def my_callback1(channel1):            #这里的channel和channel1无须赋确定值但不能不写
#    global counter1
#    if gpio.event_detected(35):
#        counter1 = counter1 + 1
#        print("B:"+counter1)
gpio.add_event_detect(counter_sc_motor_a, gpio.RISING, callback = get_motor_a_rpm) #在引脚上添加上升临界值检测再回调
#gpio.add_event_detect(35, gpio.RISING, callback = my_callback1)
gpio.cleanup()