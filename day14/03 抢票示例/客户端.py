#!/usr/bin/env python
# -*- coding:utf-8 -*-
from  multiprocessing import Process,Lock
import time
import json
import random
import os



def search():
    time.sleep(0.5)
    with open('db.json','r',encoding='utf8') as f:
        data = json.load(f)
        print('剩余票数：%s'%data.get('count'))

def buy():
    with open('db.json','r',encoding='utf8') as f1:
        data = json.load(f1)

    if data.get('count',0) > 0:
        data['count'] -= 1
        time.sleep(random.randint(1,3))

        with open('db.json','w',encoding='utf8') as f2:
            json.dump(data,f2)
        print('%s 购票成功' %os.getpid())
    else:
        print('购票失败')

def task(lock):
    search()
    lock.acquire()  #加锁
    buy()
    lock.release()  #释放锁

if __name__ == '__main__':
    mext_lock = Lock()
    for i in range(10):
        p = Process(target=task,args=(mext_lock,))
        p.start()
