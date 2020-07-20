#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import time

class A:
    Country1 = 'China'
    Country2 = 'America'

# inp = input('>>>>>>')
#
# ret = getattr(A,inp)
#
# print(ret)

def login():
    print('login')

def register():
    print('register')

ret = getattr(sys.modules[__name__],'login')

# ret()

# inp = input('>>>>').strip()
# ret = getattr(sys.modules[__name__],inp)
# ret()

#反射本模块的类

class Student:
    def __str__(self):
        return 'Student'

class Mangaer:
    def __str__(self):
        return 'Mangaer'

# inp = input('>>>>').strip()
# ret = getattr(sys.modules[__name__],inp)
# print(ret())

#反射其他导入过来的模块的对象


# ret = getattr(time,'time')
# print(ret())
#
# ret = getattr(time,'localtime')
# print(ret())


lst = ['x','y','z','e','f']

for index,i in enumerate(lst,1):
    print(index,i)
