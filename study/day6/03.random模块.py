#!/usr/bin/python
# -*- coding: utf-8 -*-
import random



def func(num=4):
    res = ''
    for i in range(num):
        num = random.randint(0,9)
        #ascii = 65-90 97-122
        alph_lower = random.randint(97,122)
        alph_upper = random.randint(65,90)
        nums = [str(num),str(chr(alph_lower)),str(chr(alph_upper))]
        print(nums)
        choice_num = random.choice(nums)
        res += str(choice_num)
    return res

result = func()
print(result)
