#!/usr/bin/python
# -*- coding: utf-8 -*-

import gevent

def eat(name):
    print('%s eat 1' %name)
    gevent.sleep(5)
    print('%s eat 2' %name)

def play(name):
    print('%s play 3' %name)
    gevent.sleep(3)
    print('%s play 4' %name)

g1 = gevent.spawn(eat,'egon')
g2 = gevent.spawn(play,name = 'egon')

gevent.joinall([g1,g2])
print('主')