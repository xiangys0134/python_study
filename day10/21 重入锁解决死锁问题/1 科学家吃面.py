#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from threading import Thread,Lock

noodle_lock = Lock()
fork_lock = Lock()

def eat1(name):
    noodle_lock.acquire()
    print('%s 抢到了面条' %name)
    fork_lock.acquire()
    print('%s 抢到了叉子'%name)
    print('%s 吃面' %name)
    noodle_lock.release()
    fork_lock.release()

def eat2(name):
    fork_lock.acquire()
    print('%s 抢到了叉子' %name)
    time.sleep(1)
    noodle_lock.acquire()
    print('%s 抢到了面条' %name)
    print('%s 吃面' %name)
    fork_lock.release()
    noodle_lock.release()

if __name__ == '__main__':
    for name in ['alex','egon','gold']:
        t_eat1 = Thread(target=eat1,args=(name,))
        t_eat2 = Thread(target=eat2,args=(name,))
        t_eat1.start()
        t_eat2.start()
