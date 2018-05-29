# coding=utf-8
import json
import urllib.request
import time
import traceback
import os
# 模拟成浏览器
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Encoding": "gbk,utf-8,gb2312",
           "Accept-Language": "zh-CN,zh;q=0.8",
           "User-Agent": "Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
           "Connection": "keep-alive"}
opener = urllib.request.build_opener()
headall = []
for key, value in headers.items():
    item = (key, value)
    headall.append(item)
opener.addheaders = headall
# 将opener安装为全局
urllib.request.install_opener(opener)
# 闵行天气代码
minhang_weather_id = '58361'
# 返回天气信息


def get_weatherlist():
    try:
        url = "http://www.nmc.cn/f/rest/real/"+minhang_weather_id
        stdout = urllib.request.urlopen(url)
        weatherInfo = stdout.read().decode('utf-8')
        jsonData = json.loads(weatherInfo)
        weatherlist = []
        # 读取JSON数据，添加到列表中
        szDate = jsonData["publish_time"]
        weatherlist.append('publish time')
        weatherlist.append(szDate)
        szCity = jsonData["station"]["city"]
        weatherlist.append(szCity)
        #print("城市: "+str(szCity))
        weatherlist.append('weather')
        szWeather = jsonData["weather"]["info"]
        weatherlist.append(szWeather)
        weatherlist.append('wind direct')
        szdirect = jsonData["wind"]["direct"]
        weatherlist.append(szdirect)
        weatherlist.append('wind speed')
        szspeed = str(jsonData["wind"]["speed"]) + "m/s"
        weatherlist.append(szspeed)
        weatherlist.append('temperature')
        szTemp = str(jsonData["weather"]["temperature"])
        weatherlist.append(szTemp)
        weatherlist.append('humidity')
        szhumidity = str(int(jsonData["weather"]["humidity"]))
        weatherlist.append(szhumidity)
        weatherlist.append('rain')
        szRain = jsonData['weather']['rain']
        weatherlist.append(szRain)

        return weatherlist
    except urllib.error.URLError as e:
        print("获取天气状况数据出现URLERROR！一分钟后重试……")
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
        time.sleep(60)
        # 出现异常则过一段时间重新执行此部分
        get_weatherlist()
    except Exception as e:
        print("获取天气状况数据出现EXCEPTION！十秒钟后重试……")
        print("Exception：" + str(e))
        traceback.print_exc()  # 获得错误行数
        time.sleep(10)
        # 出现异常则过一段时间重新执行此部分
        get_weatherlist()


def getweather():

    print("数据更新时间，天气，风向，风速，实时温度，相对湿度：")
    weatherlist = []
    weatherlist = get_weatherlist()
    print(weatherlist)
    # 保存数据格式：年月日 小时，minhang_weather
    writefiles_weather(time.strftime(
        "%Y-%m-%d %H : 00 minhang_weather", time.localtime(time.time())), weatherlist)

# 本步骤需要提前创建data_weather 文件夹


def writefiles_weather(filename, weatherlist):
    try:
        # 将获取的数据写入文件中，数据分别为数据更新时间，天气，风向，风速（m/s），实时温度（℃），相对湿度（%）。
        with open(os.path.abspath('.')+"/data_weather/"+filename+".txt", "a", errors="ignore") as f:
            for weather in weatherlist:
                f.write(str(weather))
                f.write(",")
            f.write("\n")
        print("该条天气数据已添加到文件中！")
    except Exception as e:
        print("天气状况数据写入文件函数出现异常！将跳过此部分……")
        print("Exception："+str(e))
        traceback.print_exc()  # 获得错误行数
        pass


if __name__ == '__main__':
    while(True):
        print("==========开始工作==========")
        getweather()
        print("【休息中……】")
        time.sleep(2)
