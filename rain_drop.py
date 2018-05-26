#控制雨水传感器 包含三个函数 雨水传感器返回雨水情况
#控制温度传感器 返回温度与湿度
#两个数据耦合返回温湿度数据

def tem_and_hum():
    pass

def raindrop():
    pass

def weather_measure():
    pass
    
import RPi.GPIO as gpio
import time, sys
gpio.setmode(gpio.BOARD)
raindrop_model = 7;
gpio.setup(raindrop_model,gpio.IN)

while True:
    if gpio.input(raindrop_model):
        print('not raining..')
        time.sleep(0.5)
    else:
        print('raining..')
        time.sleep(0.5)
        break
    