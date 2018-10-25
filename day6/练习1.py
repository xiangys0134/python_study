#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime,time
from dateutil.relativedelta import relativedelta

'''
安装dateutil模块
>pip install python-dateutil
>>> from dateutil.relativedelta import relativedelta
>>> from datetime import datetime, timedelta
>>> a = datetime(2012, 9, 23)
>>> a + relativedelta(months=+1)
datetime.datetime(2012, 10, 23, 0, 0)
'''


my_time1 = '2018-11-15 10:15:41'
my_time2 = '2016-11-13 10:02:03'

#输入两个字符串时间获取时间数组
my_strtime1 = time.strptime(my_time1,"%Y-%m-%d %H:%M:%S")
my_strtime2 = time.strptime(my_time2,"%Y-%m-%d %H:%M:%S")

# print(type(my_strtime1))
# print(my_strtime1)
# print(type(my_strtime1[0]))
#将时间转换为datetime格式进行换算

my_datime1 = datetime.datetime(my_strtime1[0],my_strtime1[1],my_strtime1[2],my_strtime1[3],my_strtime1[4],my_strtime1[5])
my_datime2 = datetime.datetime(my_strtime2[0],my_strtime2[1],my_strtime2[2],my_strtime2[3],my_strtime2[4],my_strtime2[5])
print(my_datime1)
print(my_datime2)


#此种方式不推荐使用只能计算对应的天数及时分秒,但是并不能换算成月日格式
my_difftime = (my_datime1 - my_datime2)
print('相差时间:',my_difftime)






