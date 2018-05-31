#!/usr/bin/python3
# coding=utf-8
# author：sundxfansky@sjtu.edu.cn
# 温湿度获取程序

#import commands
import web_weather
import threading

# 获取cpu温度


def get_cpu_temp():
    tempFile = open("/sys/class/thermal/thermal_zone0/temp")
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000


# 获取gpu温度


def get_gpu_temp():
    gpu_temp = commands.getoutput(
        '/opt/vc/bin/vcgencmd measure_temp').replace('temp=', '').replace('\'C', '')
    return float(gpu_temp)

# 获取dh11数据，返回一个数据是否正常的bool值，温度数据，湿度数据,接受引脚


def dh11_init(dh11_pin=12):
    print('initializing dh11....')
    # start work
    gpio.setup(dh11_pin, gpio.OUT)
    print('initialized dh11')


def get_dh11_tem_hum(dh11_pin=12):
    data = []
    j = 0
    # gpio.output(12,gpio.HIGH)
    # delay(10)
    gpio.output(dh11_pin, gpio.LOW)
    time.sleep(0.02)
    gpio.output(dh11_pin, gpio.HIGH)
    i = 1

    # wait to response
    gpio.setup(dh11_pin, gpio.IN)

    while gpio.input(dh11_pin) == 1:
        continue

    while gpio.input(dh11_pin) == 0:
        continue
    while gpio.input(dh11_pin) == 1:
        continue
    # get data

    while j < 40:
        k = 0
        while gpio.input(dh11_pin) == 0:
            continue

        while gpio.input(dh11_pin) == 1:
            k += 1
            if k > 100:
                break
        if k < 12:
            data.append(0)
        else:
            data.append(1)
        j += 1

    print("DH11 Sensor is working")
    # get temperature
    humidity_bit = data[0:8]
    humidity_point_bit = data[8:16]
    temperature_bit = data[16:24]
    temperature_point_bit = data[24:32]
    check_bit = data[32:40]

    humidity = 0
    humidity_point = 0
    temperature = 0
    temperature_point = 0
    check = 0
    dh11_truth = False

    for i in range(8):
        humidity += humidity_bit[i]*2**(7-i)
        humidity_point += humidity_point_bit[i]*2**(7-i)
        temperature += temperature_bit[i]*2**(7-i)
        temperature_point += temperature_point_bit[i]*2**(7-i)
        check += check_bit[i]*2**(7-i)

    tmp = humidity+humidity_point+temperature+temperature_point

    if check == tmp:
        dh11_truth = True
    else:
        dh11_truth = False

# 返回云端温度，湿度，雨水


def get_web_temp_hum():
    weather_list = []
    weather_list = web_weather.get_weatherlist()
    return float(weather_list[-5]), float(weather_list[-3]), float(weather_list[-1])


# 检测云端数据是否有雨
# 使用前设置has_already_setted_timer = False
def rain_warning():
    global has_already_setted
    tommorrow_weather = True
    #tommorrow_weather = istommorrow_rain()
    if tommorrow_weather is True:
        print("Tommorrow weather is raining ,setting timer......")
        # 防止开启过多线程
        if has_already_setted_timer is False:
            # 测试程序不开启
            #timer = threading.Timer(86400, task_main())
            has_already_setted = True
            print("Already setted timer")
        else:
            print("Already setted earlier")


def rain_drop(rain_drop_pin=7):

    # testing.....
    # print(get_web_temp_hum())
    # has_already_setted = False
    # rain_warning()
    # rain_warning()
