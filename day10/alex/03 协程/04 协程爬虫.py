#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib import request
import time
import gevent
from gevent import monkey

monkey.patch_all()

def f(url):
    print('GET %s' %url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%s bytes received from %s' %(len(data),url))

urls = ['https://www.baidu.com',
        'https://www.qq.com',
        'https://www.qidian.com'
        ]

time_start = time.time()

for url in urls:
    f(url)

print("同步cost",time.time() - time_start)

async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f,'https://www.baidu.com'),
    gevent.spawn(f,'https://www.qq.com'),
    gevent.spawn(f,'https://www.qidian.com'),
])

print("异步cost",time.time() - async_time_start)