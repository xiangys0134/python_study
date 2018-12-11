#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process,Queue
# import queue
import threading


def f(qm):
    qm.put([42,None,'hello'])
    # print('aaa')

if __name__ == '__main__':
    q = Queue()
    p = Process(target=f,args=(q,))
    # p = threading.Thread(target=f,args=(q,))
    p.start()
    p.join()


    print(q.get())