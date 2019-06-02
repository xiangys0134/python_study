#!/usr/bin/python
# -*- coding: utf-8 -*-

import time,datetime

date_onw = 1
#获取当前时间序列
my_stru = time.localtime()  #获取当前时间序列



#修改时间序列后转换成字符串时间
my_datetime = datetime.datetime(my_stru[0],my_stru[1],date_onw,my_stru[3],my_stru[4],my_stru[5])
# print(my_datetime)

#转换为时间序列
my_stru_time = time.strptime('%s'%my_datetime,"%Y-%m-%d %X")
# print(my_stru_time)

#转换为时间戳
my_stamp = time.mktime(my_stru_time)
print(my_stamp)



#获取时间戳
# time.mktime()