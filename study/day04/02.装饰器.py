#!/usr/bin/python
# -*- coding: utf-8 -*-


def wrapper(func):
    def inner(*args,**kwargs):
        print('装饰器之前')
        func(*args,**kwargs)
        print('装饰器之后')
    return inner

@wrapper
def func(a,b,c):
    print('游戏,%s %s %s'%(a,b,c))

func(1,2,3)