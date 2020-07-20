#!/usr/bin/env python
# -*- coding:utf-8 -*-

from urllib.request import urlopen

def func(url):
    ret = urlopen(url)
    content = ret.read().decode('utf-8')

    def inner():
        return content
    return inner

url = 'https://www.infoq.cn/article/DcIG3BX0DG*YrcyJCttC'

inner = func(url)

ret = inner()
print(ret)

