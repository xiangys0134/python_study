#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process,Lock
import json
import os
import time
import os
import random
import json


def search():
    time.sleep(0.5)
    with open('db','r',encoding='utf8') as f:
        f = f.read()
        data = json.loads(f)
        print('剩余票数：%s' %(data['count']))

def buy():
    with open('db','r',encoding='utf8') as f:
        f = f.read()
        data = json.loads(f)

    if data['count'] > 0:
        data['count'] -= 1
        time.sleep(random.randint(1,3))
        with open('db','w',encoding='utf8') as f2:
            f2.write(json.dumps(data))
            print('进程%s 购票成功' %(os.getpid()))
    else:
        print('购票失败')

def task():
    search()
    buy()

if __name__ == '__main__':
    for i in range(10):
        p = Process(target=task)
        p.start()

