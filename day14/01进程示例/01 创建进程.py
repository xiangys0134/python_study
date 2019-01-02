#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process
import time
import os

def task(num):
    print('%s的子进程PID：%s'%(num,os.getpid()))
    print('骑士计划开始了')
    time.sleep(3)
    print('骑士计划结束了')


if __name__ == '__main__':
    print('主进程ID：%s' %os.getpid())
    for i in range(10):
        p = Process(target=task,args=(i,))
        p.start()
    print('主进程结束了','*' * 120)