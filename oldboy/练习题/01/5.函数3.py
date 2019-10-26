#!/usr/bin/env python
# -*- coding:utf-8 -*-

#写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为{0:11,1:22,2:33}

def foo(L):
    D={}
    if isinstance(L,list):
        i = 0
        while i <len(L):
            D[i] = L[i]
            i += 1
    return D

ret = foo([1,2,3,4,5])
print(ret)
