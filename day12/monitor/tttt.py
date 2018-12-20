#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import time
str = 'console'

# # ret = re.search('[^(con)]',str)
# ret = str.startswith('con')
# print(ret)

date_time = time.time()
# time.strftime("%Y-%m-%d %X"
print(time.strftime('%Y-%m-%d %X',time.localtime(date_time)))



