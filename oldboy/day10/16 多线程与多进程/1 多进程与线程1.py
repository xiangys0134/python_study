#!/usr/bin/python
# -*- coding: utf-8 -*-

from threading import Thread
from  multiprocessing import Process
import os
import time
import random

def work():
    print('hello',os.getpid())

if __name__ == '__main__':
    #part1：在主进程下开启多个线程，每个线程跟主进程的pid一样
    t1 = Thread(target=work)
    t2 = Thread(target=work)

    t1.start()
    t2.start()

    print('主线程/主进程pid',os.getpid())


    #part2:开启多个进程，每个进程都有不同的pid
    p1 = Process(target=work)
    p2 = Process(target=work)

    p1.start()
    p2.start()

    print('主线程/主进程pid',os.getpid())