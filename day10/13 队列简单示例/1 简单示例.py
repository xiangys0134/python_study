#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Queue

q = Queue(3)

q.put(3)
q.put(3)
q.put(3)
# q.put(3)

try:
    q.put_nowait(3)
except:
    print('队列已经满了')
print(q.full())

print(q.get())
print(q.get())
print(q.get())
# print(q.get())

try:
    q.get_nowait(3)
except:
    print('队列已经空了')

print(q.empty())

"""
针对以上问题我有很大疑问：主要是队列已经取的时候或者是put的时候都会有一个值在定义，很纳闷
"""