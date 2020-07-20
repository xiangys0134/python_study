#!/usr/bin/env python
# -*- coding:utf-8 -*-

list1 = [1,[2,3]]

# for i in list1:
#     print(i)

def foo(l):
    if type(l) == list:
        for i in l:
            foo(i)
    else:
        print(l)

foo(list1)


