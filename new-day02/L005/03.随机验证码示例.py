#!/usr/bin/env python
# -*- coding:utf-8 -*-


import random


def func(n):
    lst = []
    for i in range(n):
        sts = random.randint(0,9)
        A_Z = chr(random.randint(65,90))
        a_z = chr(random.randint(97,122))

        list_random = random.choice([sts,A_Z,a_z])
        lst.append(str(list_random))

    return ''.join(lst)

ret = func(5)

print(ret)

