#!/usr/bin/python
# -*- coding: utf-8 -*-

class MyRange:
    def __init__(self,*args):
        if args:
            if len(args) == 1:
                self.start = 0
                self.atop = args[0]
                self.step = 1
            elif len(args) == 2:
                self.start = args[0]
                self.stop = args[1]
                self.step = 1
            else:
                pass
        else:
            raise ValueError('至少需要一个参数')

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            ret = self.start
            self.start += self.step
            return ret
        else:
            raise StopIteration

for i in MyRange(10,100):
    print(i)
