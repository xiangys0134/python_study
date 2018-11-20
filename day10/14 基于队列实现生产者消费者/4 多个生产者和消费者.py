#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process,Queue
import time
import os
import random

def consumer(q):
    while True:
        res = q.get()
        if res is None:break
        time.sleep(random.randint(1,3))
        print('##%s 吃了包子%s' %(os.getpid(),res))

def producer(name,q):
    for i in range(10):
        res = '%s%s' %(name,i)
        q.put(res)
        time.sleep(random.randint(1,3))
        print('%s 生产了 %s' %(os.getpid(),res))

if __name__ == '__main__':
    q = Queue()

    p1 = Process(target=producer,args=('包子',q,))
    p2 = Process(target=producer,args=('骨头',q,))
    p3 = Process(target=producer,args=('泔水',q,))

    c1 = Process(target=consumer,args=(q,))
    c2 = Process(target=consumer,args=(q,))

    p1.start()
    p2.start()
    p3.start()

    c1.start()
    c2.start()

    p1.join()
    p2.join()
    p3.join()
    q.put(None)
    q.put(None)

    print('主进程')