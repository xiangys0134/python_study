#!/user/bin/env python3
# -*- coding: utf-8 -*-

class Person:
    def __init__(self,nickname,sex,hp,aggr):
        self.name = nickname
        self.sex = sex
        self.hp = hp
        self.aggr = aggr

    def attack(self,dog):
        print('%s打了%s,%s掉了%s血'%(self.name,dog.name,dog.name,self.aggr))

class Dod:
    def __init__(self,nickname,sex,hp,aggr):
        self.name = nickname
        self.sex = sex
        self.hp = hp
        self.aggr = aggr


alex = Person('alex','不详',10,5)

哮天犬 = Dod('哮天犬','藏獒',100000,50)

alex.attack(哮天犬)

print(哮天犬.hp)