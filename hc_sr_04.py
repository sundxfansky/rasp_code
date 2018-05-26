import RPi.GPIO as GPIO
import time

#GPIO.cleanup()
#bug: 返回值为0

GPIO.setmode(GPIO.BOARD)
#Attention 
#This program is only use for Raspberry pi3B test hc_se_04 moduel
#The first or front hc_sr_04
#trig -> 11
#echo -> 13
front_trig = 29	
front_echo = 31



def distance():
	GPIO.output(front_trig,1)
	time.sleep(0.000015)
	GPIO.output(front_trig,0)
	while not GPIO.input(front_echo):
		pass
	t1 = time.time()
	while GPIO.input(front_echo):
		pass
	t2 = time.time()
	return (t2-t1)*340/2

#initial
time.sleep(1)
GPIO.setup(front_echo,GPIO.IN)
GPIO.setup(front_trig,GPIO.OUT,initial = 0)
print('Running')
for i in range(600):
	print("Distance: %0.2f m" %distance())
	time.sleep(0.05)

GPIO.cleanup()




	
