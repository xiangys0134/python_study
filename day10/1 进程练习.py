#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
import  os
import time

def task(num):
    print('子进程开始：%s'%(os.getpid()))
    time.sleep(num)
    print('子进程结束：%s'%(os.getpid()))

if __name__ == '__main__':
    start_time = time.time()
    p1 = Process(target=task,args=(3,))
    p1.daemon
    p1.start()
    print('主进程：%s 执行时间%s'%(os.getpid(),time.time() - start_time))
