#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from multiprocessing import Process
import time

x = 100

def change():
    global x
    x = 10
    time.sleep(3)
    print('子进程执行完：%s'%x)


if __name__ == '__main__':
    p = Process(target=change)
    p.start()
    p.join()
    print('主进程：%s'%x)