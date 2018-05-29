# 控制雨水传感器 包含三个函数 雨水传感器返回雨水情况
# 控制温度传感器 返回温度与湿度
# 两个数据耦合返回温湿度数据

#初始化
def raindrop_init():
    print('raindrop modle initialing')
    gpio.setup(raindrop_model, gpio.IN)
    print('raindrop modle initiated')

#检测雨水，返回True or False
def raindrop(raindrop_model_pin=7):
    if gpio.input(raindrop_model_pin):
        return False
    else:
        return True
