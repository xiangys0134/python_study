#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

def consumer():
    print('aaaa')
    while True:
        x = yield
        print('处理了数据',x)

g = consumer()
next(g)
g.send(1)
g.send(2)