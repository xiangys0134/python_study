#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from gevent import monkey;monkey.patch_all()
import time
import gevent

def eat(name):
    print('%s eat 1'%name)
    time.sleep(2)
    print('%s eat 2'%name)

def play(name):
    print('%s play 1' %name)
    time.sleep(2)
    print('%s play 2' %name)

g1 = gevent.spawn(eat,'egon')
g2 = gevent.spawn(play,'alex')

g1.join()
g2.join()

print('主')