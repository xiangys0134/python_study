#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

def outer(flag):
    def cal_time(func):
        def inner(*args,**kwargs):
            start = time.time()
            ret = func(*args,**kwargs)
            print(time.time() - start)
            return ret
        return inner
    return cal_time

@outer(True)
def func():
    time.sleep(0.1)
    print('in func')


@cal_time
def wahaha():
    time.sleep(0.1)
    print('in wahaha')


@cal_time
def qqxing():
    time.sleep(0.1)
    print('in qqxing')


func()
qqxing()