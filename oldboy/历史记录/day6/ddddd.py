#!/usr/bin/env python
# -*- coding:utf-8 -*-

# a = '(aabb)'
# b = a.strip('[()]')
# print(b)
import re
# a = '3343111.11*333'
# b = re.findall('[\+\-\*\/]',a)
# e = ''.join(b)
# print(''.join(b))

# yy = a.split(e)[0]

# print(float(yy))
# print(type(float(yy)))

a = '-111.3333*3432'
#ret = re.compile('[\-]?\d+[\.]?\d?]')
# ret = re.search('([\-]?\d+[\.]?\d+)',a).group()
# print(ret)
# tt = a.split(ret)
# print(tt)

# ret = re.compile('[\-]?\d+[\.]?\d{0,}([\+\-\*\*]+)[\-]?\d+[\.]?\d{0,}')
# ret = ret.findall(a)
# print(ret)
# print(ret)
#
# h = '11--44'
# print(h.replace('--','+'))

# a ='1'
# b = '2'
# print(a+b)
# print(len(a+b))

value = '-40/5'
#ret = re.compile('[\-]?\d+[\.]?\d{0,}([\+\-\*\*]+)[\-]?\d+[\.]?\d{0,}')
ret = re.compile('[\-]?\d+([\+\-\*\/])\d+')
b = ret.findall(value)
print(b)