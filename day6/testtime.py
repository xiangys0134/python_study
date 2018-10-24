#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from datetime import timedelta,
import datetime

# now = datetime.now()
#
# print(now.day)
# print(now)

# t1 = 11434444444444444444.333

t1 = time.time()
# print(t1)

stu_time = time.localtime(t1)   #转换为格式化时间对象

# print(stu_time)
# print(stu_time[0])
date1 = datetime.datetime(stu_time[0],stu_time[1],stu_time[2],2,23,19)
date2 = datetime.datetime(2018,5,22)
print(date1)
print(date2)
print(date1-date2)




