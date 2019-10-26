#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
通过for循环可以预先先重启确定好的进程
"""
from multiprocessing import Process
import os
import time


def task(name):
    print('%s is running' %(name))
    print('进程号：%s' %(os.getpid()))
    time.sleep(4)
    print('%s is done' %(name))

if __name__ == '__main__':
    tmp_list = []
    for i in range(10):
        p = Process(target=task,args=(i,))
        tmp_list.append(p)

    for i  in  tmp_list:
        i.daemon
        i.start()
    print('主进程：%s' %(os.getpid()))

