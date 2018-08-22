#!/usr/bin/python
# -*- coding: utf-8 -*-
flag = 100
i = 1
count = 0
while i < flag:
    if i % 2 == 0:
        count -= i
    else:
        count += i
    i += 1

print(count)



