#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re
from urllib import request

# print(re.search('func','abcfunc').group())

with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    # date = f.read()
    # re.search()
    for line in f:
        if re.search(r'http[s]://(\w+.){1,}\w+[^"]$',line.decode('utf8')):
            print(re.search(r'http[s]://(\w+.){1,}\w+[^"]$',line.decode('utf8')).group())
            re.sub(r'http[s]://(\w+.){1,}\w+[^"]$','soft.g6p.cn',line.decode('utf8'))
        print(line.decode('utf8'))

