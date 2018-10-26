#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )
'''
import re

a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

#去除最里层的值
brackets=r'\([^()]+\)'
#加法正则匹配
opp_add = r'(\d+\.?\d?+\d+\.?\d?)|(-\d+\.?\d?+\d+\.?\d?)'
#减法正则匹配
opp_sub = r'(\d+\.?\d?-d+\.?\d?)|(-\d+\.?\d?-\d+\.?\d?)'
#乘法正则匹配
opp_multi = r'(\d+\.?\d?*d+\.?\d?)|(-\d+\.?\d?*d+\.?\d?)'
#除法正则匹配
opp_div = r'(\d+\.?\d?/d+\.?\d?)|(-\d+\.?\d?/d+\.?\d?)'






#加法运算
def int_add(first,end):
    count = first + end
    return count

#减肥运算
def int_sub(first,end):
    count = first - end
    return count

#乘法运算
def int_multi(first,end):
    count = first * end
    return count

#除法运算
def int_div(first,end):
    count = first / end
    return count


