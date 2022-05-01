#!/user/bin/env python3
# -*- coding: utf-8 -*-

from  dateutil.relativedelta import relativedelta
from datetime import datetime

class Person:
    def dream(self):
        print('白日梦')

class Student:
    country = 'Channa'
    '''初始化操作'''
    def __init__(self,name,gender,birthday):
        self.name = name
        self.gender = gender
        self.birthday = birthday

    def learn(self):
        '''学习方法'''

        print('%s爱学习'%self.name)

    #属性方法
    @property
    def age(self):
        now = datetime.now()
        birthday = datetime.strptime(self.birthday,'%Y-%m-%d')
        r = relativedelta(now,birthday)
        # print(r.years)
        return r.years

    # 静态方法
    @staticmethod
    def zuodite():
        print('做地铁')

    @classmethod
    def run(self):
        print('跑步使我变强')

s1 = Student('张三','男','1995-12-01')
s2 = Student('李四','女','1995-10-01')

print(s1.country,s2.country)
s1.country = '中国'

print(s1.country,s2.country)

print(s1.age)

s1.zuodite()
Student.run()