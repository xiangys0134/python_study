#!/usr/bin/env python
# -*- coding:utf-8 -*-

def fact_iter(num,product):
    if num == 1:
        return product

    return fact_iter(num -1,num * product)

ret = fact_iter(5,1)
print(ret)

