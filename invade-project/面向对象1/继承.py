#!/user/bin/env python3
# -*- coding: utf-8 -*-

class Animal:
    def __init__(self,nickname,hp,aggr):
        print('执行init了')
        self.name = nickname
        self.hp = hp
        self.aggr = aggr
        self.sex = 'male'

    def skill(self,enemy):
        if enemy.hp > self.aggr:
            print('%s打了%s,%s掉了%s血' % (self.name, enemy.name, enemy.name, self.aggr))
        else:
            print('%s被%s打死了' % (enemy.name, self.name))


class Person(Animal):
    def __init__(self,nickname,sex,hp,aggr):
        print('Person.init')
        Animal.__init__(self,nickname,hp,aggr)
        self.sex = sex

    def attack(self,dog):
        self.skill(dog)
        # if dog.hp > self.aggr:
        #     print('%s打了%s,%s掉了%s血'%(self.name,dog.name,dog.name,self.aggr))
        # else:
        #     print('%s被%s打死了'%(dog.name,self.name))


class Dog(Animal):
    def __init__(self,nickname,kind,hp,aggr):
        Animal.__init__(self, nickname, hp, aggr)
        self.kind = kind

    def bite(self,p):
        self.skill(p)
        # if p.hp > self.aggr:
        #     print('%s咬了%s,%s掉了%s血'%(self.name,p.name,p.name,self.aggr))
        # else:
        #     print('%s被%s咬死了'%(p.name,self.name))

alex = Person('alex','不详',10,4)
# print(alex.sex)

哮天犬 = Dog('哮天犬','藏獒',1000,50)
# print(哮天犬.name)
alex.attack(哮天犬)
哮天犬.bite(alex)