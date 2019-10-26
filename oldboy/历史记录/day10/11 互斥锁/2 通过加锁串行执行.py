#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process,Lock
import time
import random

#生产一个互斥锁
mutex_lock = Lock()

def task(name,lock):
    lock.acquire()
    print('这是task %s任务' %(name))
    print('%s 进入厕所' %(name))
    time.sleep(random.randint(1,4))
    print('%s 完事了' %(name))
    time.sleep(random.randint(1,3))
    print('%s 出了洗手间' %(name))
    lock.release()

if __name__ == '__main__':
    tmp_list = []
    for i in ['alex','wusir','EJ']:
        p = Process(target=task,args=(i,mutex_lock))
        p.start()
        tmp_list.append(p)

