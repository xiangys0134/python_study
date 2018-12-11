#!/usr/bin/python
# -*- coding: utf-8 -*-

import multiprocessing
import time

def run(name):
    time.sleep(2)
    print('hello',name)

if __name__ == '__main__':
    tmp_list = []
    for i in range(10):
        p = multiprocessing.Process(target=run,args=('bob'+str(i),))
        p.start()
        tmp_list.append(p)
        # p.join()
    for i in tmp_list:
        i.join()

    print('*' * 120)
    print('主进程')
