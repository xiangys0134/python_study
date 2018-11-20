#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process,Queue
import os
import time

def inputQ(queue):
    info = str(os.getpid()) + '(put):' + str(time.asctime())
    queue.put(info)

def outputQ(queue):
    info = queue.get()
    print ('%s%s\033[32m%s\033[0m'%(str(os.getpid()), '(get):',info))

q = Queue()
inputQ(q)
outputQ(q)