#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

t1 = os.path.abspath('.')

print(t1)

with open(os.path.join(t1,'userinfo'),'w',encoding='utf-8') as f1:
    f1.write('你好，中国')

