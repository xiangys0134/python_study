#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process, Lock
import json
import time
import random
import os

# 设置互斥锁
mutex_lock = Lock()


def search():
    time.sleep(0.5)
    with open('db', 'r', encoding='utf8') as f:
        data = json.load(f)
        print('剩余票数:{}'.format(data.get('count')))


def buy():

    with open('db', 'r', encoding='utf8') as f:
        data = json.load(f)
    if data.get('count', 0) > 0:
        data['count'] -= 1
        time.sleep(random.randint(1, 3))
        with open('db', 'w', encoding='utf8') as f2:
            json.dump(data, f2)
        print('{}购票成功！'.format(os.getpid()))
    else:
        print('购票失败')


def task(lock):
    search()  # 查票并发
    lock.acquire()
    buy()  # 串行买票
    lock.release()


if __name__ == '__main__':
    for i in range(10):
        p = Process(target=task, args=(mutex_lock, ))
        p.start()