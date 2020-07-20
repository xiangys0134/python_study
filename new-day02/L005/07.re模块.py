#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 在python中利用正则表达式

import re

#re.findall()
#re.search()

ret = re.findall('\d+','2342u111')

# print(ret)


# ret = re.search('\d+','1aaa')       #search只匹配从头到尾符合条件的第一个
#
# # if ret:
# #     print(ret.group())
#
#
# ret = re.findall('\d+(?:\.\d+)?','2342u111.2456')
#
# print(ret)



ret  = re.match('\d+','1112324254fdsdf4335')

# print(ret.group())

#替换

s='alex83egon25boss.jin40'
s='alex83,egon25,boss.jin40 '

# ret = re.split('\d+',s)
# ret = re.split('[|, ]',s)
# print(ret)


# ret = re.sub('\d+','##',s,4)
# ret = re.subn('\d+','#',s)
# print(ret)


#compile

# re.compile()

ret = re.compile('\d+')

res1 = ret.findall('alex|83,egon|25,boss.jin|40')
res2 = ret.findall('alex83egon25boss.jin60')
# print(res1)
# print(res2)


#时间和空间


#时间
re_iter = ret.finditer('alex|83,egon|25,boss.jin|40')

# for i in re_iter:
#     print(i.group())


# ret = re.findall('\d\d','dgu18agej6ggf189')
# print(ret)
# ret = re.findall('\d(\d)','dgu18agej6ggf189')
# print(ret)


tab1 = '<a>wahaha</a>2321312.1215fds2.44ff456'

# ret = re.findall('<(\w)>(\w+)',tab1)
# print(ret)

ret = re.findall('<(?P<tab>\w+)>(?P<con>\w+)</(?P=tab)>',tab1)
# print(ret)

ret = re.search('<(?P<tab>\w+)>(?P<con>\w+)</(?P=tab)>',tab1)

# print(ret.group())
# print(ret.group('tab'))
# print(ret.group('con'))
# print(ret.group(2))

#可以根据分组的名字使用group('name') 取值

#在正则表达式中已经有名字的分支


ret = re.findall('\d+\.\d+|\d+',tab1)

print(ret)



#分组命名


#分组命名，验证




