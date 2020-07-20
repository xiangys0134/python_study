#!/usr/bin/env python
# -*- coding:utf-8 -*-

def func():
    print('开始了')
    yield 1
    print('又来了')
    yield 2

a = func()

print(a.__next__())
# print(a.__next__())
# print(a.__next__())


