#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
name = 'alex'
age = 34

class A:
    Country1 = 'China'
    Country2 = 'America'
    def __init__(self):
        pass

    def show_country(self,cls):
        print('hello',cls)

# inp = input('>>>')
#
# alex = A()
#
# if hasattr(alex,inp):
#     ret = getattr(alex,inp)
#     ret('张三')
# else:
#     print(inp)

def register():
    print('register')

inp = input('>>>')

ret = getattr(sys.modules[__name__],inp)
print(ret())

#反射本模块中的类



