#!/usr/bin/python
# -*- coding: utf-8 -*-
from threading import Thread
import os
import time

def foo():
    global n
    tmp = n
    time.sleep(0.1)
    n = tmp - 1

if __name__ == '__main__':
    n = 100
    tmp_list = []
    for i in range(100):
        t = Thread(target=foo)
        t.start()
        tmp_list.append(t)

    for p in tmp_list:
        p.join()

    print('主线程',n)

