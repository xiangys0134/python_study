#!/usr/bin/env python
# -*- coding:utf-8 -*-

def my_range(func,index=None,step=None):
    start_num = index if index else 0
    step = step if step else 1
    while start_num<func:
        yield start_num
        start_num += step

ret = my_range(10)

for i in ret:
    print(i)

