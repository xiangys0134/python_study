#!/usr/bin/env python
# -*- coding:utf-8 -*-

def my_len(s):
    count = 0
    for i in s:
        count += 1
    return count

# s1 = 'dfasfdsafsa2324234'
# s2 = '11111'
# print(my_len(s1)<my_len(s2))


def func(a,b,*args,default = 'male',**kwargs):
    print(a,b)
    print(args)
    print(default)
    print(kwargs)

func(1,2,3,4,name='xiangys0134',age=30)


