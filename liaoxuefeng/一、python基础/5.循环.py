#!/usr/bin/env python
# -*- coding:utf-8 -*-

names = ['Michael','Bob','Tracy']
for i in names:
    print(i)

# sum_count = 0
# x = range(1,101)
#
# for i in x:
#     print(i)
#     sum_count += i
# print(sum_count)

sum_count = 0
i = 1
flag = 1
while flag:
    sum_count += i
    i += 1
    if i==101:
        flag = False

print(sum_count)

