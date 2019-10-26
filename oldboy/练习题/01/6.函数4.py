#!/usr/bin/env python
# -*- coding:utf-8 -*-

def foo(x,y,z,q):
    with open('statudent.txt','a',encoding='utf8') as f:
       f.write('%s\t%s\t%s\t%s\n'%(x,y,z,q))

foo('张三','男',24,'大专')
foo('李四','男',24,'大专')

