#!/usr/bin/env python
# -*- coding:utf-8 -*-

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield 5

ret = odd()
# print(next(ret))
# print(next(ret))
# print(next(ret))


for i in ret:
    print(i)

