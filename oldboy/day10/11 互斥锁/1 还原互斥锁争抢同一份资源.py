#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
import time
import random
import os

def task(num):
    print('这个是 task %s 任务' %(num))
    print('%s 进了洗手间' %(num))
    time.sleep(random.randint(1,4))
    print('%s 完事了' %(num))
    time.sleep(random.randint(1,3))
    print('%s 出了洗手间' %(num))


if __name__ == '__main__':
    tmp_list = []
    for i in ['alex','gold','EJ','wusir']:
        p = Process(target=task,args=(i,))
        p.start()
        tmp_list.append(p)



