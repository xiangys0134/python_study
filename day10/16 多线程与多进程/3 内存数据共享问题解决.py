#!/usr/bin/python
# -*- coding: utf-8 -*-

from threading import Thread
from multiprocessing import Process
import os

def work():
    global n
    n = 0

if __name__ == '__main__':
    n =1
    t = Thread(target=work)
    t.start()
    t.join()

    print('主',n)