#!/user/bin/env python3
# -*- coding: utf-8 -*-

class Person:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def dear(self):
        print('%s不想上班，还有钱拿'%self.name)

obj1 = Person('张三','男')

print(hasattr(obj1,'name'))

a = getattr(obj1,'name')

print(a)



