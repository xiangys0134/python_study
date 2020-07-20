#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

#随机 验证码 抽奖 彩票

#
# lst = list(range(100))
#
# random.shuffle(lst)
#
# print(lst)
#

res = ''

for i in range(4):
    num = str(random.randint(0,9))
    ascil_A = chr(random.randint(65,90))
    ascil_a = chr(random.randint(97,123))
    # print(num,ascil_a,ascil_A)
    code = random.choice([num,ascil_a,ascil_A])
    # print(code)
    res += str(code)

print(res)


