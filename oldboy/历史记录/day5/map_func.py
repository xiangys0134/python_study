#!/usr/bin/python
# -*- coding: utf-8 -*-
dic1 = {'a':'b','x':'y'}
def my_map(x):
    return x,dic1[x]
a = map(my_map,dic1)
print(list(a))
