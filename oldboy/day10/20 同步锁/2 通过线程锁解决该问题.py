#!/usr/bin/python
# -*- coding: utf-8 -*-
from threading import Thread,Lock,current_thread
import os
import time

def foo():
    start_time1 = time.time()
    print('%s start to run' %current_thread().getName())
    global n
    lock.acquire()
    tmp = n
    time.sleep(3)
    n = tmp - 1
    lock.release()
    stop_time1 = time.time()
    print('%s sttop to run' % current_thread().getName(),stop_time1 - start_time1)

if __name__ == '__main__':
    lock = Lock()
    n = 100
    tmp_list = []
    start_time = time.time()
    for i in range(100):
        # lock.acquire()
        t = Thread(target=foo)
        t.start()
        # lock.release()
        tmp_list.append(t)

    for p in tmp_list:
        p.join()

    stop_time = time.time()
    print('主线程',start_time - stop_time,n)

