#!/usr/bin/python
# -*- coding: utf-8 -*-

import gevent
import time
from gevent import monkey

monkey.patch_all()

def eat(name):
    print('%s eat 1' %name)
    time.sleep(5)
    print('%s eat 2' %name)

def play(name):
    print('%s play 3' %name)
    time.sleep(3)
    print('%s play 4' %name)

g1 = gevent.spawn(eat,'egon')
g2 = gevent.spawn(play,name = 'egon')

gevent.joinall([g1,g2])
print('主')