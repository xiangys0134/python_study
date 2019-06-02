#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from threading import Thread
import os
import time

x =100

def task():
    global x
    x = 10
    print('子线程 开始',os.getpid())
    print('_' * 120)
    time.sleep(2)
    print('子线程结束')

if __name__ == '__main__':
    t1 = Thread(target=task)
    t1.start()
    t1.join()
    print('主线程 开始',os.getpid())
    print('=' * 120)
    print(x)