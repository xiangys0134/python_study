#!/usr/bin/python
# -*- coding: utf-8 -*-

from  multiprocessing import Process,Queue
import time
import random
import os

def consumer(q):
    while True:
        res = q.get()
        if res is None:break
        print('####%s 吃了 %s' %(os.getpid(),res))

def produce(q):
    for i in range(10):
        q.put(i)
        print('%s 生产了包子%s' %(os.getpid(),i))

if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=produce,args=(q,))

    c1 = Process(target=consumer,args=(q,))

    p1.start()
    c1.start()

    p1.join()
    q.put(None)
    print('主进程')
