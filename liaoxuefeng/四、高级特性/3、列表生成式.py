#!/usr/bin/env python
# -*- coding:utf-8 -*-

g = (x * x for x in range(1,10))

try:
    while 1:
        print(next(g))
except StopIteration as e:
    pass
    # print('except',e)