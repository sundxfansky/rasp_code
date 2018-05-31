import RPi.GPIO as gpio
import time
import sys
gpio.setmode(gpio.BOARD)
motor_a = 18
motor_b = 32
#Speed ​​feedback
#2relaymodel
switch1 = 36
switch2 = 38


gpio.output(switch2, gpio.HIGH)
gpio.output(switch1, gpio.HIGH)
