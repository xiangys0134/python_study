#!/usr/bin/env python 
# -*- coding: utf-8 -*-

class Lol():
    def __init__(self,my_ali,her_ali):
        self.my_ali = my_ali
        self.her_ali = her_ali

    def kill(self,envs):
        return '%s in %s kill %s'%(self.my_ali,envs,self.her_ali)

abc = Lol('亚瑟','猴子')
ret = abc.kill('草丛')
print(ret)