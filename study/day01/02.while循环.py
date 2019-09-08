#!/usr/bin/python
# -*- coding: utf-8 -*-
# flag = True
# while flag:
#     print(111)
#     print(222)
#     flag = False
#     print(333)

flag = 1
count = 0
int_seq =1
while flag:
    count += int_seq
    int_seq += 1
    if int_seq > 100: flag = False
print(count)
