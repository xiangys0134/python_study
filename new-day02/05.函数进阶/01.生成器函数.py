#!/usr/bin/env python
# -*- coding:utf-8 -*-


def func():
    print('开始啦')
    yield 1
    print('又来了')
    yield 2
    print('再来一次')
    yield 3



s1 = func()
next(s1)
next(s1)
next(s1)





