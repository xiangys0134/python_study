#!/usr/bin/python
# -*- coding: utf-8 -*-

from threading import Thread
import time

def foo():
    print(123)
    time.sleep(2)
    print('end123')

def bar():
    print(456)
    time.sleep(2)
    print('end456')

if __name__ == '__main__':

    t1 = Thread(target=foo)
    t2 = Thread(target=bar)

    t1.daemon=True
    t1.start()
    t2.start()

    print('主线程')