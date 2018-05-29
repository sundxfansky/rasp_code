#!/usr/bin/python3
#coding=utf-8
#author：sundxfansky@sjtu.edu.cn

def motor_init(motor_a=18,motor_b=32):
    print('motor inicializing .....')
    gpio.setup(motor_a, gpio.OUT)
    gpio.setup(motor_b, gpio.OUT)
    prnt('motor inicialized')

