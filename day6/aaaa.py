#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
# a = '-8.7'
# ret = re.compile('[\-]?(\d+)')
# ret =ret.findall(a)
# print(a)

# ret = re.findall('\d+[\.]?\d{0,}',a)[0]
# print(ret)

# ret = re.search('[\-]?(\d+)',a)
#
# print(ret)

str1 = '-9/3'

# first_ret = re.search('(\d+[\.]?\d{0,})([\*\/])([\-]?\d+[\.]?\d{0,})', str1).span()[0]
# second_ret = re.search('(\d+[\.]?\d{0,})([\*\/])([\-]?\d+[\.]?\d{0,})', str1).span()[1]
# count_str1 = re.search('(\d+[\.]?\d{0,})([\*\/])([\-]?\d+[\.]?\d{0,})', str1).group().strip('[()]')
#
# print(first_ret)
# print(second_ret)
# print(count_str1)

# ret = re.findall('[-]?\d+[\.]?\d{0,}',str1)
#
# if len(ret) == 1:
#     print('aaa')
# print(len(ret))
# print(ret)

#ret = re.compile('[\+\-]?(\d+[\.]?\d{0,})[\*\/][\-]\d+[\.]?\d{0,}')
# ret = re.compile('4\-(\d+[\.]?\d{0,})[\*\/]([\-]?\d+[\.]?\d{0,})')
# ret = ret.findall(str1)
# # ret = re.search('(\d+[\.]?\d{0,})[\*\/]([\-]\d+[\.]?\d{0,})',str1)
# print(ret)

ret = re.findall('[\-]?(\d+[\.]?\d{0,})([\+\*\/\-])(\d+[\.]?\d{0,})',str1)

# ret = re.findall('[-]?\d+[\.]?\d{0,}',str1)
# print(len(ret))
print(ret)