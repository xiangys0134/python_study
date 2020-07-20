#!/usr/bin/env python
# -*- coding:utf-8 -*-

# lst = ['型号','机型','配置','序列号']


with open('test.txt','r',encoding='utf-8') as f, \
    open('new1.txt','a',encoding='utf-8') as f1:
    for line in f:
        res = line.split(',')
        # print(str(res)+ '\"')
        lst = []
        for i in res:
            res = '"' + str(i.strip()) +'"'
            lst.append(str(res))
        # print(lst)
        ret = ";".join(lst)
        print(ret)
        # print(ret)
        f1.write(ret)
        f1.write("\n")


        # print(ret)

# print(lst)