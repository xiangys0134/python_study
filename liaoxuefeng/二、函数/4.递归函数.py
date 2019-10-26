#!/usr/bin/env python
# -*- coding:utf-8 -*-

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

ret = fact(100)

print(ret)




