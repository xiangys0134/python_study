#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
安装dateutil模块
>pip install python-dateutil
>>> from dateutil.relativedelta import relativedelta
>>> from datetime import datetime, timedelta
>>> a = datetime(2012, 9, 23)
>>> a + relativedelta(months=+1)
datetime.datetime(2012, 10, 23, 0, 0)

'''

from dateutil.relativedelta import relativedelta
