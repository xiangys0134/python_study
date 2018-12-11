#!/usr/bin/python
# -*- coding: utf-8 -*-

import multiprocessing
import threading
import time

def run(name):
    time.sleep(2)
    print('%s 吃包子' %name)
    t = threading.Thread(target=run_thead,args=())
    t.start()
    t.join()
    print('主线程')

def run_thead():
    # print(threading.Thread.getName())
    print(threading.get_ident())
    print('我是一个线程')

if __name__ == '__main__':
    tmp_list = []
    for i in range(10):
        p = multiprocessing.Process(target=run,args=('小明' + str(i),))
        p.start()
        tmp_list.append(p)

    for p in tmp_list:
        p.join()

    print('*' * 120)
    print('主进程')