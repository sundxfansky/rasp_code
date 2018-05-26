import RPi.GPIO as gpio
import time, sys

#我用的第12个引脚
pin = 18

gpio.setmode(gpio.BOARD)
gpio.setup(pin, gpio.OUT)

#频率设置为400Hz
p = gpio.PWM(pin, 400)

p.start(5)

#占空比从10开始，逐渐加到90
time.sleep(2);
gpio.output(pin,True)
p.ChangeDutyCycle(10)
time.sleep(1);
p.stop()
gpio.cleanup()
