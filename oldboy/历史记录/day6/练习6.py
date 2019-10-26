#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
获取当前文件所在目录
'''
import os,sys

# a = os.path.dirname('d:\\env2.7\\pip-selfcheck.json')
# print(a)
#
# os.path.exists()

def dir_file(dirs):
    if os.path.isfile(dirs):
        return os.path.dirname(dirs)
    else:
        return 0

a = dir_file('d:\\env2.7\\pip-selfcheck.json')
print(a)