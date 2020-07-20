#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Persion:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return self.name

    def dream(self):
        print('%s不想上班，还有钱拿'%self.name)

p1  = Persion('张三','男')
p2 = Persion('李四','男')

p1.dream()

print(p1,p2)




