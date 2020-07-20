#!/usr/bin/env python
# -*- coding:utf-8 -*-

def my_pop(l,index=None):
    index = index if index else 0
    print(l.pop(index))

list1 = [1,2,3]

my_pop(list1,2)

