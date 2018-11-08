#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    1.创建一个武松，武松可以打老虎、杀嫂子
	2.用面向对象的思维来模拟王者荣耀中亚瑟上阵杀敌
	3.用面向对象的思维来实现用户登录
"""

#创建一个武松，武松可以打老虎、杀嫂子
# class Person:
#     """
#     定义Person类
#     """
#     def __init__(self,name):
#         self.name = name
#
#     def sha(self,user):
#         print('%s杀%s'%(self.name,user))
#
#     def da(self,animal):
#         print('%s打%s'%(self.name,animal))
#
#
# # wusong = Person('武松')
# # wusong.da('老虎')
# # wusong.sha('嫂子')


#用面向对象的思维来模拟王者荣耀中亚瑟上阵杀敌
# class Lol:
#     """
#     生产一个游戏类
#     """
#     def __init__(self,name):
#         self.name = name
#
#     def kill_one(self,kill_one):
#         print('%s使用了第一技能%s'%(self.name,kill_one))
#
#     def kill_two(self,kill_two):
#         print('%s使用了第二技能%s'%s(self.name,kill_two))
#
#     def kill_three(self,kill_three):
#         print('%s使用了第三技能%s'%(self.name,kill_three))
#
#
# yase = Lol('亚瑟')
# yase.kill_one('跳杀')
# yase.kill_one('旋转')
# yase.kill_one('一刀暴击')

#用面向对象的思维来实现用户登录
class Account:
    def __init__(self,user,password):
        self.user = user
        self.passowrd = password

    def login(self):
        if self.user == 'user' and self.passowrd == '123':
            print('%s登录成功'%(self.user))
        else:
            print('登录失败')

user1 = Account('user','123')
user1.login()