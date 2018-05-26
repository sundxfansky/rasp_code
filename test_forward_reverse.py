import RPi.GPIO as GPIO
import time , sys

GPIO.setmode(GPIO.BOARD)
#给定初始值
GPIO.setup(36, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(38, GPIO.OUT, initial = GPIO.LOW)
time.sleep(2)
print("opening....")
GPIO.output(36,GPIO.HIGH)
GPIO.output(38,GPIO.HIGH)

time.sleep(10)

GPIO.cleanup()


