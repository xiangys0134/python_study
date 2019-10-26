#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
在当前目录下创建一个文件夹、在这个文件夹下创建一个文件
'''

import os,sys

def mkdir_files(dirs,files):
    for i in "*" "/" "\\" " ":
        if i in dirs:
            return 0
    if os.path.exists(dirs) == False:
        os.mkdir(dirs)
        os.system('echo "aaa"> %s'%(os.path.join(dirs,files)))
        return 1

a = mkdir_files('test1234','aa.txt')
# a = mkdir_files('/','aa.txt')
print(a)