#!/usr/bin/env python
# -*- coding:utf-8 -*-

l1 = [1,2,2,1,3,4,5,3]

# print(list(set(l1)))

s1 = {1,2,3}
s2 = {1,4,5}

#取并集
print(s1|s2)


#取交集
print(s1&s2)

#取差集
print(s1-s2)

#取对称差集
print(s1^s2)