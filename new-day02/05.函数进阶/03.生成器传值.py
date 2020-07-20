#!/usr/bin/env python
# -*- coding:utf-8 -*-


def eat(name):
    print('%s 在吃东西'%name)
    while 1:
        try:
            food = yield
            print('%s在吃%s'%(name,food))
        except StopIteration:
            break
s1 = eat('alex')

print(s1.__next__())
s1.send('红烧肉')
s1.send('西瓜')
