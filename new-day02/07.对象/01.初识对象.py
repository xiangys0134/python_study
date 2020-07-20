#!/usr/bin/env python
# -*- coding:utf-8 -*-

from math import pi

class Car():
    def __init__(self,name,p1,color):
        self.name = name
        self.pl = p1
        self.color = color

    def run(self,speed):
        print('%s车速很快,坐好扶稳 时速：%s迈'%(self.name,speed))


# fll = Car('法拉利','5.0T','红色')
# bsj = Car('保时捷','3.0T','黑色')
#
#
# fll.run(300)
# bsj.run(260)
#
#
# print(fll.run,bsj.run)
# print(id(fll.run),id(bsj.run))


class Circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

    def perimeter(self):
        return 2 * pi * self.radius


c1 = Circle(10)

print('面积',c1.area())
print('周长',c1.perimeter())










