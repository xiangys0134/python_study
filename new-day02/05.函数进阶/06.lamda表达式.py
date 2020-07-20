#!/usr/bin/env python
# -*- coding:utf-8 -*-

def bar():
    print('我是bar函数')

def foo():
    bar()
    print('我是foo函数')

foo()