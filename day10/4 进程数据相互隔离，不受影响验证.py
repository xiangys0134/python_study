#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
import os
import time
import random

x = 100

def task(name):
    global x
    x = 10
    print('进程开始：%s 进程号：%s' %(name,os.getpid()))
    time.sleep(random.randint(1,4))
    print('进程结束：%s 进程号：%s' %(name,os.getpid()))


if __name__ == '__main__':
    start_time = time.time()
    tmp_list = []
    for i in range(5):
        p = Process(target=task,args=(i,))
        tmp_list.append(p)

    for p in tmp_list:
        p.start()
        # p.join()

    for p in tmp_list:
        p.join()

    print('主进程：%s 执行时间：%s X：%s' %(os.getpid(),time.time() - start_time,x))


