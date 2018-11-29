#!/usr/bin/env python
# -*- coding:utf-8 -*-
import gevent

def func1():
    print('func1 running')
    gevent.sleep(2)
    print('switch func1')

def func2():
    print('func2 running')
    gevent.sleep(1)
    print('switch fun2')

def func3():
    print('func3 running')
    gevent.sleep(0)
    print('func3 done...')

gevent.joinall([
    gevent.spawn(func1),
    gevent.spawn(func2),
    gevent.spawn(func3),
]

)
