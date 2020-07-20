#!/usr/bin/env python
# -*- coding:utf-8 -*-


# 给add添加一个装饰器，如果add的两个数a,b是计算过的值，那么不要用add再计算一次，而是把之前计算过的值直接返回

def wrapper(func):
    dic = {}
    def inner(*args,**kwargs):
        s1 = args if args else tuple(kwargs.values())

        if s1 in dic:
            return dic[s1]
        else:
            ret = func(*args,**kwargs)
            dic[s1] = ret
            return ret
    return inner

@wrapper
def add(a,b):
    print('装饰器执行')
    return a + b

s1 = add(1,2)
s2 = add(1,2)
s3 = add(a=1,b=2)
s4 = add(b=2,a=1)

print(s1,s2,s3,s4)

