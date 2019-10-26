#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

def func1():
    while True:
        print('func1')
        yield

def func2():
    g = func1()
    for i in range(10):
        #i + 1
        next(g)
        time.sleep(3)
        print('func2')

start_time = time.time()
func2()
stop_time = time.time() - start_time

print(stop_time)