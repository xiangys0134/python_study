#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

def func1():
    for i in range(10):
        print('这是我第%s次打印啦' %(i))
        time.sleep(1)

def func2():
    for k in range(10):
        print('哈哈，这是我第%s次打印啦' %k)
        time.sleep(1)

#在不写入yield的时候就是单线程执行
func1()
func2()