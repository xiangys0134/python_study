#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Animal(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):return self.name+" " + str(self.age)

ret = Animal("alex",12)
egon = Animal("egon",12)

print(ret)
print(egon)


