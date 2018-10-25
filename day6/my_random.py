#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

#获取随机数
print(random.random())

#获取一个数字范围的随机数
print(random.uniform(10,20))

#返回随机整数
print(random.randint(1,20))

#跳着取值
print(random.randrange(1,9,step=2))

#从给定的迭代中选出一个
print(random.choice(list(range(1,34))))

#随机返回多个值，返回的个数为函数的第二个参数,返回的值为一个列表
print(random.sample(range(1,34),6))

#写一个指定的随机验证码
def valie(num):
    tmp = []
    for i in range(num):
        rand_int = str(random.randrange(0,9))
        rand_asci_up = chr(random.randrange(65,91))
        random_asci_low = chr(random.randrange(97,123))
        num_st = random.choice([rand_int,rand_asci_up,random_asci_low])
        tmp.append(num_st)
    return ''.join(tmp)

a = valie(5)
print(a)