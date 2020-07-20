#!/usr/bin/env python
# -*- coding:utf-8 -*-

# class Goods:
#     __discount = 0.8
#     discount = 0.8
#
#
# #带双下划线都是私有的
#
# print(Goods.discount)
# print(Goods.__discount)


class Goods:
    def __init__(self,o_price):
        self.__price = o_price


    def get_price(self):
        return self.__price

apple = Goods(5)

print(apple.get_price())





