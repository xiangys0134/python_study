#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import re
#
# a = 'aa ddd ggg'
# ret = re.sub('\s+','-',a,count=1)
#
# print(ret)

a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'

# ret = re.search('\d+[\.]?\d{0,}([\*\/]+)[\-]?\d+[\.]?\d{0,}',a).group()
# print(ret)


b = a.replace(' ','')
print(b)
b = '-3.1*4*27'
#ret = re.findall('[-]?\d+\.?\d{0,}[\*\/\+\-]\d+\.?\d{0,}',b)
#ret = re.findall('[-]?\d+[\.]?\d{0,}[\*\/\+\-]',b)
ret = re.findall(r'[-]?\d+[.]?\d{0,}[*/][-]?\d+[.]?\d{0,}',b)

#ret = re.findall(r'[-]?\d+[.]?\d{0,}([*/])[-]?\d+[.]?\d{0,}',b)[0]
ret = re.search(r'[-]?\d+[.]?\d{0,}[*/][-]?\d+[.]?\d{0,}',b).group()
ret = ret.split('*')
print(ret)

a = '1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
ret = re.search(r'\(?([^()]+).*\)?',a)
print(ret)
# ret = re.sub(r'([^()]+)','aaa',a,1)
# print(ret)
# if ret:
#     print('yes')
# else:
#     print('no')

# count = 20
# if count >= 0:
#     count = r'+' + str(count)
#
# print(count)
# print(type(count))
