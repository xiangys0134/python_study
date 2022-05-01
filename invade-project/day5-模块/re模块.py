#!/user/bin/env python3
# -*- coding: utf-8 -*-

import re

ret = re.search(r'^\d+','4324fdsa432313433dfsaf')

# ret = re.findall('\d+','34234fdfdsa332424')
# print(ret)

#match

# ret = re.match('\d+','fdsa432342423fafds323')

# print(ret)

s = 'alex83egon25bossjin342'
ret = re.split(r'\d+',s)

# print(ret)

ret  = re.compile(r'\d+')

# res1 = ret.findall('fdsafdsa34324324fdsafd34242')
# print(res1)


ret = re.findall('www.baidu.com|www.oldboy.com','www.oldboy.com')
ret = re.findall('www.(?:baidu|oldboy).com','www.oldboy.com')
print(ret)

ret = re.findall('\d+(?:\.\d+)?','1.23+4.35')
print(ret)