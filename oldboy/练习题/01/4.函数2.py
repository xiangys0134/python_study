#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
d1 = {}
def foo(D):
    if isinstance(D,dict):
        for k,v in D.items():
            if len(v)>2:
                d1[k] = v[:2]
            else:
                d1[k] = v
dic = {"k1": "v1v1", "k2": [11,22,33,44]}

foo(dic)

print(d1)

