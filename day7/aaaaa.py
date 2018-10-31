#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import pi

class Circle:
    '''
    定义一个园类型
    '''
    def __init__(self,radius):  #self表示对象也是就是c1  即c1 =
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

c1 = Circle(3)
print(c1.area())
print(c1.perimeter())


