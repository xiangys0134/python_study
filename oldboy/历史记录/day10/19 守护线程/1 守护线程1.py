#!/usr/bin/python
# -*- coding: utf-8 -*-

from threading import Thread
import time

def sayhi(name):
    time.sleep(2)
    print('%s say hello' %name)

if __name__ == '__main__':
    t = Thread(target=sayhi,args=('egon',))
    t.daemon=True   #必须在t.start()之前设置
    t.start()
    t.join()
    print('主线程')
    print(t.is_alive())