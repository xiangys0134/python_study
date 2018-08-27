#!/usr/bin/python
# -*- coding: utf-8 -*-

# import time
# now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# print(type(now_time))
# dic = {}
# dic["123"] = now_time
# print(dic)
#

d1 = {"1.2":'201','2.5':'ddd'}
print(max(d1),type(max(d1)))
print(d1[max(d1)])



dc = {}
#获取cpu负载信息
def load_avg():
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f1 = open('/proc/loadavg','r')
    allavg = f1.readline()
    load_1 = allavg.split()[0]
    print load_1,now_time
    dc[load_1] = now_time
    f1.close()
    #return load_1