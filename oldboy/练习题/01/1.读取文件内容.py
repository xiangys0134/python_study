#!/usr/bin/env python
# -*- coding:utf-8 -*-

L=[]
D={}
list1 = ['序号','部门','人数','平均年龄','备注']


with open('a1.txt',encoding='utf8') as f:
    for line in f:
        flg = 0
        while flg < len(line.split()):
            D[list1[flg]] = line.split()[flg]
            flg += 1
        print(D)
        L.append(D)

        print(L)

        # print(line)

print(L)









