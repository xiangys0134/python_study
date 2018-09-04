#!/usr/bin/env python
# -*- coding:utf-8 -*-
#yousong.xiang 2018.9.5
#v1.0.1

import os

tmp_file = 'student_tump'
f = open('student','r',encoding='utf-8')
for i in f:
    print(i)

l1 = ['id','name','age','phone','job']
#传递三个参数分别 select name, age where age>22  值为：age > 20 name age
def select_sql(field,ope,value,*args):
    #判断文件是否存在,如果存在则删除
    if os.path.exists(tmp_file):
        os.remove(tmp_file)
    file2 = open(tmp_file,'a',encoding='utf-8')
    if str(value).isdigit():
        value = int(value)

    #获取字段值信息
    field_id = l1.index(field)

    #判断传入运算符是否为">"
    if ope == '>':
        for i in f:
            field_list = i.split(',')
            if field_list[field_id] > value:
                file2.write(','.join(i))
            file2.close()
            f.close()

    #判断传入运算符是否为"="
    if ope == '=':
        for i in f:
            field_list = i.split(',')
            if field_list[field_id] == value:
                file2.write(','.join(i))
            file2.close()
            f.close()

    #判断传入运算符是否为"like"
    if ope == 'like':
        for i in f:
            field_list = i.split(',')
            if value in field_list[field_id]:
                file2.write(','.join(i))
            file2.close()
            f.close()

    #对字段进行判断
    l2 = []
    with open(tmp_file,'r',encoding='utf-8') as file2:
        if "*" in args:
            for i in file2:
                l2.append(i)
            return l2
        else:
            pass

