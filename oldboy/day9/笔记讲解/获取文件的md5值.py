# -*- coding: utf-8 -*-
# @Time    : 2018/11/11 0011 18:29
# @Author  : Luffy
# @Email   : customer@luffycity.com
# @File    : 获取文件的md5值.py
# @Software: PyCharm

import hashlib


md5_obj = hashlib.md5()
with open('day09课上笔记.txt', 'rb') as f:
    for i in f:
        md5_obj.update(i)

print(md5_obj.hexdigest())
