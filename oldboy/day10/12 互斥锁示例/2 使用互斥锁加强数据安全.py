#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process,Lock
import time
import os
import random
import json

#设置互斥锁
mutex_lock = Lock()


#查询余票
def search():
    time.sleep(random.randint(1,3))
    with open('db','r',encoding='utf8') as f:
        f = f.read()
        data = json.loads(f)
        print('拥有票数：%s' %(data['count']))

def buy():
    # lock.acquire()
    # time.sleep(random.randint(2,5))
    with open('db','r',encoding='utf8') as f:
        f = f.read()
        data = json.loads(f)
    if data['count'] > 0:
        print(data['count'])
        with open('db','w',encoding='utf8') as f2:
            data['count'] -= 1
            data = json.dumps(data)
            f2.write(data)
    print('%s 购票成功' %(os.getpid()))
    # lock.release()


def task(lock):
    search()
    lock.acquire()
    buy()
    lock.release()

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=task,args=(mutex_lock,))
        p.start()
    print('-主进程-')


