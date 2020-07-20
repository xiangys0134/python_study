#!/usr/bin/env python
# -*- coding:utf-8 -*-

def wrapper1(func):
    def inner1(*args,**kwargs):
        print('wrapper1 开始')
        ret = func(*args,**kwargs)
        print('wrapper1 结束')
        return ret
    return inner1

def wrapper2(func): #func = qqxing
    def inner2(*args,**kwargs):
        print('wrapper2 开始')
        ret = func(*args,**kwargs)  #qqxing()
        print('wrapper2 结束')
        return ret
    return inner2    #qqxing


@wrapper1   #qqxing = wrapper1(wrapper2(qqxing))        ->wrapper1(inner2)
@wrapper2   #qqxing = wrapper2(qqxing)
def qqxing():
    print('qqxing..')

qqxing()

