#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Person():
    def __new__(cls, *args, **kwargs):
        print('调用__new__,创建类实例')
        return super().__new__(Person)

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def eat(self):
        print('%s在吃东西'%(self.name))

p1 = Person('张三','男')
p1.county = 'CHINA'
# print(p1.__dict__)
# print(Person.__dict__)

# if hasattr(Person,'')

Person.name = 'China'
print(Person.name)

a = setattr(Person,'sb','test')
print(Person.sb)

b = setattr(p1,'name','中国')
print(p1.name)


