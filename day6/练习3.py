#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
生成一个6位随机验证码(包含数字和大小写字母)
'''
import random

def valie(num):
    tmp = []
    for i in range(num):
        rand_int = str(random.randrange(0,9))
        rand_asci_up = chr(random.randrange(65,91))
        random_asci_low = chr(random.randrange(97,123))
        num_st = random.choice([rand_int,rand_asci_up,random_asci_low])
        tmp.append(num_st)
    return ''.join(tmp)

a = valie(6)
print(a)
