#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle

dic = {'k1':'v1','k2':'v2','k3':'v3'}
str_dic = pickle._dumps(dic)
print(str_dic)

with open('a','wb') as f:
    f.write(str_dic)

with open('a','rb') as f:
    a = f.read()
print(a)

dic2 = pickle.loads(a)
print(dic2)