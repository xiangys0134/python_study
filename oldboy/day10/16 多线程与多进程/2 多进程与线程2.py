#!/usr/bin/python
# -*- coding: utf-8 -*-

from threading import Thread
from multiprocessing import  Process
import os
import time
import random

def work():
    print('hello',os.getpid())

if __name__ == '__main__':
    #在主进程下开启线程
    t = Thread(target=work)
    t.start()
    print('##主线程/主进程',os.getpid())

    #在主进程下开启子进程
    t = Process(target=work)
    t.start()
    print('主线程/主进程',os.getpid())