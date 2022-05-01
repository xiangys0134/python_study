#!/user/bin/env python3
# -*- coding: utf-8 -*-


class Person:
    Country = 'China' #静态变量
    def __init__(self,name,hp,agger):
        self.name = name
        self.hp = hp
        self.agger = agger

    def action(self):   #动态变量
        print('in action',self.name)

alex = Person('alex',100,30)
egon = Person('egon',200,23)

alex.action()
print(alex.name)

print(alex.Country)
Person.action(alex)