#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process,Pool
import time
import os


def Foo(name):

    print('hello world',os.getpid())
    time.sleep(1)
    return name + 100

if __name__ == '__main__':
    pool = Pool(5)
    # freeze_support()
    for i in range(10):
        pool.apply(func=Foo,args=(i,))

    print('end')
    pool.close()
    pool.join()


