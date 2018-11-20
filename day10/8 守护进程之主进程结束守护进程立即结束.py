#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
import time
import random

def foo(name):
    print('守护进程：%s' %(name))
    time.sleep(random.randint(1,5))
    print('end')

if __name__ == '__main__':
    start_time = time.time()
    tmp_list = []
    for i in range(2):
        p = Process(target=foo,args=(i,))
        p.daemon = True
        p.start()
        tmp_list.append(p)
    time.sleep(4)
    print('主进程',time.time() - start_time)
