#!/usr/bin/python
# -*- coding: utf-8 -*-

import time,datetime

#以下就表示为时间戳
# print(time.time())
# t = time.time()
# print(int(t))

#时间字符串
# print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strptime('2018-10-22 12:12:54',"%Y-%m-%d %H:%M:%S"))

# print(time.localtime())

# print(datetime.datetime(2018,10,11))

time_tuple = time.localtime(1500000000)
print(time.mktime(time_tuple))