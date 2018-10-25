#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
计算某路径下所有文件和文件夹的总大小
'''
import os,sys

def tmp_dirs(dis):
    if os.path.exists(dis) and os.path.isdir(dis):
        tmp_lists = os.listdir(dis)
        print(tmp_lists)
        size_count = 0
        for i in tmp_lists:
            size_count += os.path.getsize(os.path.join(dis,i))
        return size_count

a = tmp_dirs('d:\\')
print(a)