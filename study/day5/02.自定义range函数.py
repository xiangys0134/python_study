#!/usr/bin/python
# -*- coding: utf-8 -*-

def my_range(start,stop,step=1):
    
    n = start
    while n < stop:
        yield n
        n += step

for i in my_range(10,20,2):
    print(i)

