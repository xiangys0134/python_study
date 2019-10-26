#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Pool
import time
import os

def Foo(name):
    time.sleep(3)
    print('hello world',os.getpid(),name)

def Bar(i):
    print('x--->args:',i,os.getpid())


if __name__ == '__main__':
    pool = Pool(processes=3)
    print('主进程:',os.getpid())

    for i in range(10):
        pool.apply_async(func=Foo,args=(i,),callback=Bar(i))

    pool.close()
    pool.join()

