#!/usr/bin/python3
#coding=utf-8
#author：sundxfansky@sjtu.edu.cn

def sonar_distance(sonar_echo=29,sonar_trig=31):
	GPIO.output(sonar_trig,1)
	time.sleep(0.000015)
	GPIO.output(sonar_trig,0)
	while not GPIO.input(sonar_echo):
		pass
	t1 = time.time()
	while GPIO.input(sonar_echo):
		pass
	t2 = time.time()
	return (t2-t1)*340/2

def ultra_sonar_a_init(sonar_a_echo=29,sonar_a_trig=31):
	print('initializing ultra sonar a.....')
	gpio.setup(sonar_a_echo, gpio.IN)
	gpio.setup(sonar_a_trig, gpio.OUT, initial=0)
	print('initialized ultra sonar a')

def ultra_sonar_b_init(sonar_b_echo=11, sonar_b_trig=13):
	print('initializing ultra sonar b .....')
	gpio.setup(sonar_b_echo, gpio.IN)
	gpio.setup(sonar_b_trig, gpio.OUT, initial=0)
	print('initialized ultra sonar b')

#测试
# time.sleep(1)
# print('Running')
# for i in range(600):
# 	print("Distance: %0.2f m" %distance())
# 	time.sleep(0.05)
# GPIO.cleanup()





	
