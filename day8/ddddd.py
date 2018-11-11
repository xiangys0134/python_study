#!/usr/bin/env python 
# -*- coding: utf-8 -*-

class Foo(object):

    staticField = "old boy"

    def __init__(self):
        self.name = 'wupeiqi'

    def func(self):
        return 'func'

    @staticmethod
    def bar():
        return 'bar'

# print(getattr(Foo, 'staticField'))
# print(getattr(Foo, 'func'))
# print(getattr(Foo, 'bar'))

import sys

def s1():
    print('s1')

def s2():
    print('s2')

this_module = sys.modules[__name__]

print(hasattr(this_module,'s1'))
print(getattr(this_module,'s2'))
