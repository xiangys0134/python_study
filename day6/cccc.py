#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
str1 = re.sub('[-]?\d+[\.]?\d{0,}[+-][-]?\d+[\.]?\d{0,}','###','abc1234323+2',1)


# print(str1)

# def abc(str1,count=0):
#     count = 32.0
#     if count == 32.1:
#         return 111
#     else:
#         return count
# a = abc('-32.0')
# print(a)

# a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
# #first1 = re.findall('\([^()]+\)',a)[0].strip('()')
# first1 = re.findall('\([^()]+\)',a)
# print(first1)


a = eval('1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )')
print(a)

# # a = '1-5*4/2+4-9'
# ret = re.sub('\d+[/*]\d+','aaa',a,1)
# print(ret)