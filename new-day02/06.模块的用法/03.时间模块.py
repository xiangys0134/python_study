#!/usr/bin/env python
# -*- coding:utf-8 -*-


import time
#1.时间戳

print(time.time())
#
# print(time.strftime('%Y-%m-%d %X'))


#结构化时间
# print(time.localtime())

#互相转换
# 1.时间戳--->结构化时间
t1 = 1585119335.618847

print(time.gmtime(t1))
print(time.localtime(t1))


#结构化时间--->时间戳

t2 = time.localtime(t1)

print(time.mktime(t2))



