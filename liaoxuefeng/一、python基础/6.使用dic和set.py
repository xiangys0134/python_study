#!/usr/bin/env python
# -*- coding:utf-8 -*-

d = {'Michael':95,'Bob':75,'Tracy':85}
print(d.get('Michael11'))

if 'Michael' in d:
    print('存在')
else:
    print('不存在')


s = {1,2,3}
print(s,type(s))