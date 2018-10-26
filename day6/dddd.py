#!/usr/bin/python
# -*- coding: utf-8 -*-

# import random
#
# print(random.randrange(1,2))


import re
#去除最里层的值
brackets=r'\([^()]+\)'

a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
a = '12344'
# print(a[18:25])
# print(a[:18])
# print(a[25:])
# # tt = re.compile(brackets)
# # b = tt.findall(a)
# #
# # print(b)
# c = re.search(brackets,a).span()
# d = re.search(brackets,a).group()
# print(c)
# print(d)


# tt = re.compile(brackets)
# b = tt.findall(a)
# print(b)

# a = '111  gdsgfds 55445'
# print(re.sub('\s+','',a))
# # print(a.replace('\s+',''))

# a = '9-2*5/3+7/3*99/4*2998+10*568/14'
# #a = 'fdsafsa'
# # ret = re.compile('(\d+)([\*\/])([\-]?\d+)')
# # ret = ret.findall(a)
# # print(ret)
#
# # ret = re.search('[\-]?\d+[]]')
#
# ret = re.search('(\d+)([\*\/])([\-]?\d+)',a)
# print(ret)


a = '+43'
# ret =re.search('[\+\-]',a).group()
# print(ret)

ret = re.compile('[\+\-]')
ret = ret.findall(a)
print(ret)

# ret = a.split('[+-]')
# print(ret)
# print()