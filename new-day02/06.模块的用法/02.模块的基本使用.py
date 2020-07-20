#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import namedtuple

t1 = (1,2)


#用元组表示一个坐标

t = (1,2)   #不够形象

Point = namedtuple('zb',['x','y'])

print(Point(1,2))






