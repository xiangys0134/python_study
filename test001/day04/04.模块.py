#!/usr/bin/env python
# -*- coding:utf-8 -*-


import time

# print(time.time())      #单位是秒
#
#
# #时间戳格式 1970年
#
# ret = time.strftime('%Y-%m-%d %H:%M:%S')
#
# print(ret)
#
# print(time.localtime())
# time.sleep(2)
#
# rtime = time.time()
#
# #时间戳时间转格式化
#
#
#
# time_local = time.localtime(rtime)
#
# print(time.strftime('%Y-%m-%d %H:%M:%S',time_local))


time.time()

#1991.8.2  转时间戳
#1988.12.7 转时间戳


w_time = time.strptime('1991.8.2','%Y.%m.%d')
m_time = time.strptime('1988.12.7','%Y.%m.%d')
print(w_time)
print(m_time)

wmk_time = time.mktime(w_time)
mmk_time = time.mktime(m_time)

strtime = wmk_time - mmk_time

print(strtime)
m,s = divmod(strtime,60)
h,m = divmod(m,60)
d,h = divmod(h,24)
# print(d,h,m,s)



str = time.strftime('%Y-%m-%d')

print(str)








