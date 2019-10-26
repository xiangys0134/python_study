#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from multiprocessing import Process,Lock
import time

mutex_locak = Lock()

def talk(name,lock):
    lock.acquire()
    print('%s 进入厕所'%(name))
    print('%s 上厕所'%(name))
    print('%s 完事'%(name))
    print('%s 出厕所'%(name))
    lock.release()

if __name__ == '__main__':
    p1 = Process(target=talk,args=('alex',mutex_locak))
    p2 = Process(target=talk,args=('gold',mutex_locak))
    p3 = Process(target=talk,args=('wu',mutex_locak))

    p1.start()
    p2.start()
    p3.start()
