#!/usr/bin/python
# -*- coding: utf-8 -*-
from threading import Thread
import os
import time
import random

def sayhi(name):
    time.sleep(2)
    print('%s say hello' %name )

if __name__ == '__main__':
    t = Thread(target=sayhi,args=('egon',))
    t.start()
    print('主线程')