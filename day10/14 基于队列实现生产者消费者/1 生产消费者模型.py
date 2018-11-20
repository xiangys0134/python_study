#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process,Queue
import time
import random
import os

def consumer(q):
    while True:
        res = q.get()
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))

def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res = '包子%s'%(i)
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=producer,args=(q,))

    c1 = Process(target=consumer,args=(q,))

    p1.start()
    c1.start()

    print('----主进程----')

"""
此时的问题是主进程永远不会结束，原因是：生产者p在生成完成后就结束了。但是消费者c在取空了之后，一直处于死循环中
"""