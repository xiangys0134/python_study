#!/usr/bin/env python
# -*- coding:utf-8 -*-
from multiprocessing import Process
import time

def task1():
    print('任务1开始')
    time.sleep(3)
    print('任务1结束')

def task2():
    print('任务2开始')
    time.sleep(5)
    print('任务2结束')

if __name__ == '__main__':
    start_time = time.time()
    print('主进程 开始')
    p1 = Process(target=task1)
    p2 = Process(target=task2)

    p2.daemon = True

    p1.start()
    p2.start()

    p1.join()
    print('主进程结束')
    print(time.time() - start_time)