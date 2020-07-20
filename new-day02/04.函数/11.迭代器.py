#!/usr/bin/env python
# -*- coding:utf-8 -*-

def my_for(arg):
    # print(arg)
    y = arg.__iter__()
    while 1:
        try:
            print(y.__next__())
        except Exception as e:
            print(e)
            break

l1 = [1,2,3,4,5]

my_for(l1)


# y = l1.__iter__()

# print(y.__next__())
# print(y.__next__())


