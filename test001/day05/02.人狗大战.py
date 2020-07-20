#!/usr/bin/env python
# -*- coding:utf-8 -*-

#class

#创建一个父类
class Animal:
    def __init__(self,name,hp,aggr):
        print('执行init了')
        self.name = name
        self.hp = hp
        self.aggr = aggr
        self.sex = 'male'

    def skill(self,enemy):
        if enemy.hp > self.aggr:
            enemy.hp -= self.aggr
            print('%s咬了%s,%s 掉了%s血,还剩%s'%(self.name,enemy.name,enemy.name,self.aggr,enemy.hp))
        else:
            enemy.hp = 0
            print('%s被%s咬死了'%(enemy.name,self.name))


class Persion(Animal):
    def __init__(self,name,sex,hp,aggr):
        super().__init__(name,hp,aggr)
        self.sex = sex

    def attack(self,dog):
        self.skill(dog)



class Dog(Animal):
    def __init__(self,name,kind,hp,aggr):
        super().__init__(name,hp,aggr)
        self.kind = kind

    def bite(self,p):
        self.skill(p)

xiaotianque = Dog('哮天犬','藏獒',10000,50)

alex = Persion('alex','不详',200,5)
egon = Persion('egon','女',30,10)

alex.skill(xiaotianque)

xiaotianque.skill(egon)

