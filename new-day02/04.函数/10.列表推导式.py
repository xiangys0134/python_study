#!/usr/bin/env python
# -*- coding:utf-8 -*-

l1 = [1,-2,3,-4,5]

l2 = [ abs(i) for i in l1 ]

# print(l2)

ret = [i**2 for i in range(30) if i%3 == 0]

print(ret)


