import RPi.GPIO as gpio
import time
import sys
#pwm
gpio.setmode(gpio.BOARD)
motor_a = 18
motor_b = 32
#Speed ​​feedback
#2relaymodel
switch1 = 36
switch2 = 38

gpio.setup(switch1, gpio.OUT, initial=gpio.HIGH)
gpio.setup(switch2, gpio.OUT, initial=gpio.HIGH)
#gpio.setup(swith2,gpio.OUT,initial = gpio.LOW)


def turn_on_motor():
    print("Turn on motor....")
    time.sleep(1)
    gpio.output(switch1, gpio.LOW)
    #gpio.output(switch2,gpio.HIGH)
    print("sucessful opened")


def turn_off_motor():
    print("Turn off motor....")
    gpio.output(switch1, gpio.HIGH)
    time.sleep(0.5)
    #gpio.output(switch2,gpio.HIGH)
    print("sucessful closed")
#shun


def turn_back_motor():
    print("turning LEFT....")
    time.sleep(0.5)
    gpio.output(switch2, gpio.HIGH)
    #gpio.output(switch2,gpio.LOW)

#nishizhen


def turn_forward_motor():
    print("turning RIGHT....")
    time.sleep(0.5)
    gpio.output(switch2, gpio.LOW)
    #gpio.output(switch2,gpio.LOW)


gpio.setup(motor_a, gpio.OUT)
gpio.setup(motor_b, gpio.OUT)
#turn_on_motor()

n = 35
time1 = 5
time2 = 7
turn_on_motor()
turn_back_motor()
#频率设置为400Hz
motor_a_pwm = gpio.PWM(motor_a, 400)
motor_b_pwm = gpio.PWM(motor_b, 400)
motor_a_pwm.start(n)
motor_b_pwm.start(n)
time.sleep(time1)
motor_a_pwm.stop()
motor_b_pwm.stop()
turn_off_motor()
print(" stay...")
