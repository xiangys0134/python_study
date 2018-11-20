#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process,Queue
import time
import random
import os

def consumer(q):
    while True:
        res = q.get()
        if res is None:break
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))

def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res = '包子%s'%i
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))
    q.put(None) #发送结束信号

if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=producer,args=(q,))

    c1 = Process(target=consumer,args=(q,))

    p1.start()
    c1.start()

    print('---主进程----')
