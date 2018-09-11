#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# a = 50
# def test():
#     global a
#     a = 60
#     print(a)
# test()

def func(a):
    print(a)
    def ddd():
        print('bbbbb')
    ddd()

func('5')