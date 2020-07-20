#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

def warpper(func):
    def inner(*args,**kwargs):
        print('%s 执行了%s'%(time.strftime("%Y-%m-%d %H:%M:%S"),func.__name__))
        ret = func(*args,**kwargs)
        return ret
    return inner

@warpper
def select():
    print('打印日志')

@warpper
def delete():
    print('删除日志')

s1 = select()

d1 = delete()

print(s1)
print(d1)