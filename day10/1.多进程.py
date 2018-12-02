#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os,time

def task(mun):
    print('子进程：%s'%(os.getpid()))
    print('骑士计划，开始了')
    time.sleep(3)
    print('骑士计划，结束了')

if __name__ == '__main__':
    print('主进程：%s'%(os.getpid()))
    for i in range(10):
        p = Process(target=task,args=(i,))
        p.start()




