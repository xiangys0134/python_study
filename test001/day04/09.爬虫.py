#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib.request import urlopen

ret = urlopen('https://blog.g6p.cn/archives/552.html')

# print(ret.read().decode('utf-8'))


with open('blog.html','w',encoding='utf-8') as f:
    f.write(ret.read().decode('utf-8'))

