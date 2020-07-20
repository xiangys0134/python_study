#!/usr/bin/env python
# -*- coding:utf-8 -*-


#打开的文件句柄

with open("file",'r',encoding='utf8') as f1:
    while 1:
        try:
            print(f1.__next__(),end='')
        except StopIteration as e:
            break




