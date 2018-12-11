#!/usr/bin/python
# -*- coding: utf-8 -*-

from greenlet import greenlet

def eat(name):
    print('%s eat 1' %name)
    g2.switch('taibai')
    print('%s eat 2' % name)
    g2.switch()

def play(name):
    print('%s paly 1' %name)
    g1.switch()
    print('%s play 2' %name)

g1 = greenlet(eat)
g2 = greenlet(play)

g1.switch('taibai')

#协程还有一个玩意就是只用第一次穿一个参数，之后就不再需要进行传参
#这种情况如果swith到其他函数执行时遇到IO阻塞，一样会将现场阻塞



