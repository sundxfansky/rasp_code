#!/usr/bin/python3
# coding=utf-8
# author：sundxfansky@sjtu.edu.cn

import RPi.GPIO as gpio
import time
import sys
import tem
import switch
import rain_drop
import ultra_sonar
import motor_drive

motor_a = 18
motor_b = 32
# Speed ​​feedback
sc_motor_a = 7
sc_motor_b = 16
counter_sc_motor_a = 0  # 左轮脉冲初值
counter_sc_motor_b = 0  # 右轮脉冲初值
# raindrop_model
raindrop_model_pin = 7
# ultrasonic detection Module
sonar_a_trig = 11
sonar_b_trig = 29
sonar_a_echo = 13
sonar_b_echo = 31
# 2relaymodel
swith1 = 36
swith2 = 38

dh11_pin = 12

# 初始化引脚


def gpio_init():
    print("initializing gpio....")
    gpio.setmode(gpio.BOARD)
    print('initialized gpio.....')


gpio_init()
tem.dh11_init(dh11_pin)
switch.switch_init(swith1,swith2)
ultra_sonar.ultra_sonar_a_init(sonar_a_echo,sonar_a_trig)
ultra_sonar.ultra_sonar_b_init(sonar_b_echo,sonar_b_trig)
motor_drive.motor_init(motor_a,motor_b)
