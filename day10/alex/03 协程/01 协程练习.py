#!/usr/bin/env python
# -*- coding:utf-8 -*-
from greenlet import greenlet
import time

def test1():
    print(12)
    time.sleep(1)
    gr2.switch()
    print(34)
    gr2.switch()

def test2():
    print(56)
    gr1.switch()
    time.sleep(1)
    print(78)

gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()

