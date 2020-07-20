#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

# print(random.random())
# print(random.uniform(10,20))
# print(random.randint(1,10))
# print(random.randrange(1,10))
#
# print(random.choice(range(33)))
#
# list1 = []
#
# while 1:
#     if len(list1) == 6:
#         break
#     s1 = random.choice(range(1,33))
#     if s1 not in list1:
#         list1.append(s1)
# print(list1)
#
#
# print(random.sample(range(1,33),6))

#随机验证码

def valid_code(num):
    temp = []
    for i in range(num):
        #1.从0-9 随机一个
        i = random.randint(0,9)
        c1 = chr(random.randint(65,90))
        c2 = chr(random.randint(97,122))
        a = random.choice([i,c1,c2])
        temp.append(str(a))
    return ''.join(temp)


ret = valid_code(5)
print(ret)


