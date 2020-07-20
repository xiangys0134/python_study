#!/usr/bin/env python
# -*- coding:utf-8 -*-


#随机：验证码

import random

# print(random.random())
#
# print(random.uniform(1,3))

# print(random.randint(0,9))
#
# print(random.choice([1,2,3,4,5]))

# lst = list(range(100))
#
# random.shuffle(lst)
#
# print(lst)



def func(n):
    lst = []
    for i in range(n):
        sts = random.randint(0,9)
        A_Z = chr(random.randint(65,91))
        a_z = chr(random.randint(97,123))

        list_random = random.choice([sts,A_Z,a_z])
        lst.append(str(list_random))

    return ''.join(lst)

ret = func(5)

print(ret)

