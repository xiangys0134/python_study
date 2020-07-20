#!/usr/bin/env python
# -*- coding:utf-8 -*-

# s1 = round(3.5)
# s2 = round(4.5)
# # print(s1,s2)
#
#
# def func():
#     pass
#
# print(callable(func))
#
# print(chr(97))
#
# s2 = eval('4*6+3')
#
# print(s2)

#
# list1 = ['a','b','c']
# for x,y in enumerate(list1):
#     print(x,y)
#
# s1 = {1,2,7,4,3,8,7}
#
# print(max(s1))


list3 = [
    {'name':'alex','age':9000},
    {'name':'gold','age':35},
    {'name':'Eva-J','age':18},
    {'name':'nazha','age':19},
]

#按照年龄从小到大把list排序
def my_sort(arg):
    return arg['age']

ret = sorted(list3,key=lambda arg:arg['age'])

# print(ret)

list1 = [11,22,33,44]
list2 = ['a','b','c','d']

ret = zip(list1,list2)
ret = list(ret)
# print(list(ret))

# print(ret)
#
#
# #解包*
# s2 = list(zip(*ret))
# print(s2)

keys = ['name','age','hobby']
values = ['alex',9000,'吹牛逼']

# print(list(zip(keys,values)))

list1 = [1,2,3,4,5]

ret = map(lambda arg:arg+100,list1) #对list1中的每个元素都执行一个+100的操作

# print(list(ret))

def my_map(func,x):
    list_temp = []
    for i in x:
        list_temp.append(func(i))
    return list_temp

ret = my_map(lambda arg:arg+100,list1)
# print(ret)

list2 = [100,200,-300,400,-600]

# ret = map(abs,list2)
#
# print(list(ret))

# filter()
list2 = [100,60,70,40,65,96]

ret = filter(lambda arg:arg>90,list2)

# print(list(ret))



list1 = ['alex','gold','Eva-J']
list2 = ['alex','gold','xiaowu']

ret = filter(lambda arg:arg in list1,list2)

print(list(ret))




