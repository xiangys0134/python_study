#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process,Queue
import time

def f(q):
    q.put([time.asctime(),'hi','hello'])

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f,args=(q,))
    p.start()
    print(q.get())
    p.join()
"""
通过此种方式可以通过子进程调用然后再
"""