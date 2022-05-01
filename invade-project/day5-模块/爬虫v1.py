#!/user/bin/env python3
# -*- coding: utf-8 -*-


from urllib.request import urlopen


ret = urlopen('https://cs.newhouse.fang.com/house/s/b92/')
ret = urlopen('https://blog.g6p.cn/archives/708.html')


with open('fang.html','w',encoding='utf-8') as f:
    f.write(ret.read().decode('utf-8'))