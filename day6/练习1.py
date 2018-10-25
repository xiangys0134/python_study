#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

'''
安装dateutil模块
>pip install python-dateutil
>>> from dateutil.relativedelta import relativedelta
>>> from datetime import datetime, timedelta
>>> a = datetime(2012, 9, 23)
>>> a + relativedelta(months=+1)
datetime.datetime(2012, 10, 23, 0, 0)
'''

t2 = datetime.datetime(2017, 4, 16, 21, 21, 20)

# t1 = datetime(2018,1,21,12,23,12)
print(t2)