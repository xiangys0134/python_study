#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
a = 1562809985.7339997


local_time = time.localtime(a)
# local_time = time.localtime('%Y-%m-%d %H:%M:%S',a)
print(local_time)

str_time = time.strftime('%Y-%m-%d %H:%M:%S',local_time)
print(str_time)