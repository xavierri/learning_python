#-*-coding:utf-8-*-
import urllib2
import json
from city import city  #前一个city是模块 city.
#后一个city是模块里的变量名
cityname=raw_input('你想查哪个城市的天气？\n')  #'你想查哪个城市的天气为默认参数'
citycode=city.get(cityname)
if citycode:
        url=('http://www.weather.com.cn/data/cityinfo/%s.html'%citycode)
        content=urllib2.urlopen(url).read()
        #print type(content),此时content的类型为json字符串
        data=json.loads(content)
        #通过json.load转换程python对象，此时类型为字典
        result=data['weatherinfo']
        str_temp=('%s\n%s ~ %s')%(
            result['weather'],
            result['temp1'],
            result['temp2']
        )
        print str_temp

else:
        print'没有找到城市'




