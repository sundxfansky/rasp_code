import RPi.GPIO as gpio
import time
import sys


sc_motor_a = 7
sc_motor_b = 16
counter_sc_motor_a = 0  # 左轮脉冲初值
counter_sc_motor_b = 0  # 右轮脉冲初值

def motor_rpm_init():
    gpio.setup(sc_motor_a, gpio.IN, pull_up_down=gpio.PUD_UP)  # 读取左轮脉冲数据,加入上拉电阻保护
    gpio.setup(sc_motor_b, gpio.IN, pull_up_down=gpio.PUD_UP)  # 读取右轮脉冲数据，加入上拉电阻保护

def get_motor_a_rpm(channel):  # 边缘检测回调函channal 不用赋值
    global counter_sc_motor_a  # 设置为全局变量
    if gpio.event_detected(sc_motor_a):  # 检测到一个脉冲则脉冲数加1
        counter_sc_motor_a = counter_sc_motor_a + 1
        # print(counter_sc_motor_a)

def get_motor_b_rpm(channel):  # 边缘检测回调函channal 不用赋值
    global counter_sc_motor_b  # 设置为全局变量
    if gpio.event_detected(sc_motor_b):  # 检测到一个脉冲则脉冲数加1
        counter_sc_motor_b = counter_sc_motor_b + 1

def motor_a_rpm():
    counter_sc_motor_a_earlier = counter_sc_motor_a
    a = time.time()
    b = time.time()
    looptime = 0.03
    ppr = 47
    while True:
        if (b-a) <= looptime:
            motor_a_rpm = (counter_sc_motor_a -
                           counter_sc_motor_a_earlier)/(looptime*ppr*60)
            break
        else:
            b = time.time()
    return motor_a_rpm


def motor_b_rpm():
    counter_sc_motor_b_earlier = counter_sc_motor_b
    a = time.time()
    b = time.time()
    looptime = 0.03
    ppr = 47
    while True:
        if (b-a) <= looptime:
            motor_b_rpm = (counter_sc_motor_b -
                           counter_sc_motor_b_earlier)/(looptime*ppr*60)
            break
        else:
            b = time.time()
    return motor_b_rpm

def start_motor_a_rpm_detect():
    gpio.add_event_detect(counter_sc_motor_a, gpio.RISING,
                        callback=get_motor_a_rpm)  # 在引脚上添加上升临界值检测再回调

def remove_motor_a_rpm_detect():
    gpio.remove_event_detect(counter_sc_motor_a)


def start_motor_b_rpm_detect():
    gpio.add_event_detect(counter_sc_motor_b, gpio.RISING,
                          callback=get_motor_b_rpm)  # 在引脚上添加上升临界值检测再回调

def remove_motor_b_rpm_detect():
    gpio.remove_event_detect(counter_sc_motor_b)

