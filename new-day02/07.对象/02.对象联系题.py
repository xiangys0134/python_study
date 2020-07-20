#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Person:
    def __init__(self,name):
        self.name = name

    def da(self,obj):
        print('我是%s,我打%s'%(self.name,obj))

    def sha(self,obj):
        print('我是%s,我杀%s'%(self.name,obj.name))



# wusong = Person('武松')
# pjl = Person('潘金莲')
# wusong.da('老虎')
# wusong.sha(pjl)


class Hero:
    def __init__(self,name):
        self.name = name

    def jn_1(self):
        print('使用技能1')

    def jn_2(self):
        print('使用技能2')

    def jn_3(self):
        print('使用技能3')


yase = Hero('亚瑟')

# yase.jn_1()
# yase.jn_2()
# yase.jn_3()


# class Account:
#     def __init__(self,name,password):
#         self.name = name
#         self.password = password
#
#     def login(self,name,pwd):
#         if name == self.name and pwd == self.password:
#             print('登陆啦')
#         else:
#             print('登陆失败')
#
#
# c1 = Account('alex','123')
#
# c1.login('alex','123')


class BingXiang:
    def __init__(self,name):
        self.name = name

    def open_door(self):
        print('%s冰箱门打开'%self.name)

    def close_door(self):
        print('%s冰箱门关闭'%self.name)


class Animal:
    def __init__(self,name):
        self.name = name

    def enter(self,obj):
        print('我是%s，我自己走进了%s冰箱'%(self.name,obj.name))

haier = BingXiang('海尔')
daxiang = Animal('大象')

haier.open_door()
daxiang.enter(haier)
haier.close_door()



