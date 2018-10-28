#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import re
#
# a = 'aa ddd ggg'
# ret = re.sub('\s+','-',a,count=1)
#
# print(ret)

a = '9-2*5/3+7/3*99/4*2998+10*568/14'

ret = re.search('\d+[\.]?\d{0,}([\*\/]+)[\-]?\d+[\.]?\d{0,}',a).group()
print(ret)
