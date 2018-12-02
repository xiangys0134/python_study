#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from multiprocessing import Process
import os,time

def task1(num):
    print('子进程：%s开始'%os.getpid())
    time.sleep(3)
    print('子进程：%s结束'%os.getpid())

def task2(num):
    print('子进程：%s开始'%os.getpid())
    time.sleep(5)
    print('子进程：%s结束'%os.getpid())


if __name__ == '__main__':
    print('主进程 %s开始'%(os.getpid()))
    p1 = Process(target=task1,kwargs={'num':1})
    p2 = Process(target=task2,kwargs={'num':2})
    p1.daemon = True
    p2.daemon = True
    p1.start()
    p2.start()
    p1.join()
    # p2.join()
    print('主进程 %s结束' %(os.getpid()))