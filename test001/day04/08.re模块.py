#!/usr/bin/env python
# -*- coding:utf-8 -*-


import re

# ret = re.findall('(\d+\.\d+)',r'fdsa3.33fdsafsaf\fdsafs\fds23.4324324fdsafsaf')
# print(ret)
#
#
#
# ret = re.findall('\d+(\.\d+)?','fdsafdsa1.23fdsaf2.4')
# print(ret)
#
# ret = re.search('\d+(\.\d+)?','fdsafdsa1.23fdsaf2.4')
#
# print(ret)
#
# print(ret.group(0))
#
#
#
# ret = re.search(r'<(\w+)>\w+</\1>','<h1>fdsafdsafsa</h1>')
#
# print(ret.group())
#
#




ret = re.findall(r'\d+\.\d+|(\d+)','1-2*(60+(-40.35/5)-(-4*3))')

print(ret)

ret.remove('')

print(ret)




























