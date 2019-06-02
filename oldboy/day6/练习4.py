#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
发红包、制定金额和个数随机分配红包金额
以下写法存在bug，位于26行如果随机值取到后不为整数则会出现报错
'''
import random

#通过函数将红包个数金额组成列表
def red_envelope(money,num):
    if str(money).isdigit():
        money_count = int(money) * 100
    else:
        return 0

    if str(num).isdigit():
        num = int(num)
    else:
        return 0

    #随机获取红包个数
    tmp_list = []
    i = 1
    while num >= i:
        if num != 1:
            aof = random.randrange(1,money_count + 1)
            tmp_list.append(aof/100)
            money_count -= aof
            num -= 1
        else:
            tmp_list.append(money_count/100)
            return tmp_list

a = red_envelope(100,10)
print(a)








