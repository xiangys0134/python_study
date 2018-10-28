#!/usr/bin/env python 
# -*- coding: utf-8 -*-

class W_name():
    def __init__(self,name):
        self.name = name

    def kill(self,ani):
        #print('%s kill %s'%(self.name,ani))
        return '%s kill %s'%(self.name,ani)

abc = W_name('武松')
ret1 = abc.kill('老虎')
ret2 = abc.kill('嫂子')

print(ret1)
print(ret2)