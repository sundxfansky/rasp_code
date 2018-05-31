import RPi.GPIO as GPIO 
import time
GPIO.setmode(GPIO.BOARD)
#给定初始值
GPIO.setup(36, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(38, GPIO.OUT, initial = GPIO.HIGH)
time.sleep(2)
print("opening....")
GPIO.output(36,GPIO.LOW)
GPIO.output(38,GPIO.LOW)
time.sleep(10)
GPIO.cleanup()
