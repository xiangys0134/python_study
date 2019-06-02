#!/usr/bin/python
# -*- coding: utf-8 -*-

list1 = [1,2,3,4,5,6,7,8]

def my_filter(x):
    if x > 5:
        return True
    else:
        return False

a = filter(my_filter,list1)
print(a)
print(list(a))