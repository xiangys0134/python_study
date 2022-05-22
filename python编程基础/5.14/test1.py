#!/user/bin/env python3
# -*- coding: utf-8 -*-

import random

def func(num=4):
    str1 = ''
    for i in range(num):
        ret  = random.randrange(0,9)
        str1 += str(ret)

    return str1

# a = func(6)
# print(a)

import os

# ret = os.path.abspath(r'tes1.py')
# print(os.path.split(ret))

ret = [ x for x in range(1,101) if x%2 == 0 ]
print(sum(ret))