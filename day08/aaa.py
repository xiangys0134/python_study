#!/usr/bin/env python
# -*- coding:utf-8 -*-

# class Car:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     def run(self):
#         print('跑起来')

# c1 = Car()
#
# print(c1,type(c1))
#
# isinstance()

# #第二版
#
# class Car:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     def run(self):
#         print('%s跑起来'%self.name)
#
#
# #str1 = input('请输入你要查找的方法:').strip()
# str1 = 'run'
#
# if hasattr(Car,str1):
#     ret = getattr(Car,str1)
#     print(ret)
#     a = Car('特斯拉','电动车')
#     print(a)
#     ret(a)

# import imaplib,importlib
#
# func = importlib.import_module('aaa')
# print(func)
# func.aaa()

# class A:
#     def __init__(self,name):
#         self.name = name
#
#     def A(self):
#         print('aaaa')
#
#     def __str__(self):
#         return 'qqq'
#
# a1 = A('张三')
#
# print(a1)

class A:
    def __init__(self,name):
        self.name = name

    def aa(self):
        pass

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__['key'] = value

a1 = A('张三')
a1.age = 12
# print(a1.__dict__)
# print(a1['name'])
a1['gender'] = '男'
print(a1.__dict__)