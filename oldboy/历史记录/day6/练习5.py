#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
分别列出给定目录下所有的文件和文件夹
'''
import sys,os

def dir_tmps(dirs):
    if os.path.exists(dirs):
        return os.listdir(dirs)
    else:
        return 0

a = dir_tmps('d:\\')
print(a)
