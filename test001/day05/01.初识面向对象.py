#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Persion:
    Country = 'China'

    def __init__(self,name,sex,hp,aggr):
        self.name = name
        self.sex = sex
        self.hp = hp
        self.aggr = aggr

    def action(self):
        print('in action')

# print(Persion.Country)

#创建一个对象
alex = Persion('alex','不详',100,5)



# 2 .创建一个对象

print(alex.sex)


