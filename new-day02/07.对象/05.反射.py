#!/usr/bin/env python
# -*- coding:utf-8 -*-

class daliu:
    def __init__(self):
        pass
    def chi(self):
        print("大牛一顿吃100个螃蟹")

    def he(self):
        print("大牛一顿喝100频可乐")

    def la(self):
        print("大牛不用拉")

    def shui(self):
        print("大牛一次睡一年")

    def country(self):
        print('国家')



# func = input('输入：').strip()
# #
# # a = daliu()
# # ret = getattr(daliu,func)
# #
# # ret1 = hasattr(daliu,func)
# # print(ret())
# # print(ret1)

s1 = 'country'
cl = daliu()
ret = getattr(daliu,s1)

print(ret)
print(ret(cl))


