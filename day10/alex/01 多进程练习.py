#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process
import threading
import time

def run_thead():
    print(threading.get_ident())

def run(name):
    time.sleep(1)
    print('%s 吃了包子' %name)
    t1 = threading.Thread(target=run_thead)
    t1.setDaemon(True)
    t1.start()
    t1.join()

if __name__ == '__main__':
    tmp_list = []
    for i in range(10):
        t1 = threading.Thread(target=run,args=('小王'+str(i),))
        t1.start()
        tmp_list.append(t1)

    for thead in tmp_list:
        thead.join()

    print('主进程')