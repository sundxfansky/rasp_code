import RPi.GPIO as gpio
import time, sys
gpio.setmode(gpio.BOARD)
#pwm
motor_a = 18 
motor_b = 32
#Speed ​​feedback
motor_a_sc = 16 
motor_b_sc = 22 
# 2 relay model
relay_IN1 = 38
relay_IN2 = 36
#raindrop_model 
raindrop_model_do = 7
#ultrasonic detection Module
sonic_a_trig = 11
sonic_b_trig = 29
sonic_a_echo = 13
sonic_b_echo = 31 
#2relaymodel
swith1 = 36
swith2 = 38

gpio.setup(swith1,gpio.OUT,initial = gpio.LOW)
#gpio.setup(swith2,gpio.OUT,initial = gpio.LOW)

def turn_RIGHT_motor():
    print("RIGHT....")
    time.sleep(2)
    gpio.output(swith1,gpio.HIGH)
    #gpio.output(swith2,gpio.HIGH)
    print("sucessful opened") 

def turn_LEFT_motor():
    print("turning LEFT....")
    time.sleep(2)
    gpio.output(swith1,gpio.LOW)
    #gpio.output(swith2,gpio.LOW)

gpio.setmode(gpio.BOARD)
gpio.setup(motor_a, gpio.OUT)
gpio.setup(motor_b, gpio.OUT)
#turn_on_motor()
turn_RIGHT_motor()
#频率设置为400Hz
motor_a_pwm = gpio.PWM(motor_a , 400)
motor_b_pwm = gpio.PWM(motor_b , 400)
motor_a_pwm.start(10)
motor_b_pwm.start(10)
time.sleep(2)
motor_a_pwm.ChangeDutyCycle(20)
motor_b_pwm.ChangeDutyCycle(20)
time.sleep(2)
motor_a_pwm.stop()
motor_b_pwm.stop()

turn_LEFT_motor()
motor_a_pwm.start(10)
motor_b_pwm.start(10)
time.sleep(2)
motor_a_pwm.stop()
motor_b_pwm.stop()

gpio.cleanup()
