#!/usr/bin/env python
# -*- coding:utf-8 -*-

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n = n + 1
    return 'done'

ret = fib(100)

try:
    while True:
        print(next(ret))
except StopIteration as e:
    print(e)
