#!/usr/bin/python
# -*- coding: utf-8 -*-

class Person():
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def __hash__(self):
        "返回对象的属性个数"
        #return len(self.__dict__)
        return hash(self.name)+hash(self.gender)

p1 = Person('张三','男')
print(hash(p1))