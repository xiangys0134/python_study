#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
import os
import time

def task(name):
    print('%s is running' %(name))
    time.sleep(3)
    print('%s is running' %(name))

if __name__ == '__main__':
    p = Process(target=task,args=('t1',))
    p.start()
    print('___主进程____')