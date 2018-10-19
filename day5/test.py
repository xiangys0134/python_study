#!/usr/bin/python
# -*- coding: utf-8 -*-

l = [1,2,3,4,5]
list1 = l.__iter__()
# print(list1.__next__())
# print(list1.__next__())
# print(list1.__next__())
# print(list1.__next__())
# print(list1.__next__())
# # print(list1.__next__())
# # print(list1.__next__())


# dir = { '商品':'苹果','价格':2000 }
# dir_list = dir.__iter__()
#
# while True:
#     try:
#         print(next(dir_list))
#     except StopIteration:
#         pass
#
# list1 = range(1,100)
#
#
#
# def my_rang(*args,setep=1):
#     if len(args) == 2:
#         start = args[0]
#         stop = args[1]
#     elif len(args) == 1:
#         start = 0
#
#
# def my_iter():
#     yield 5
# a = my_iter()
# print(type(my_iter()))
#
# a.__next__()
#
# list1 = [1,2,3,4,5]
# list1 = list1.__iter__()
# list1.__next__()

# a = (( x for x in range(101)))
# print(a)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())



def my_range():
    print('aaaaa')
    n = 0
    while 1:
        yield  n
        n += 1
# my_range = my_range()
# print(my_range.__next__())
# print(my_range.__next__())
# print(my_range.__next__())
# print(my_range.__next__())


# def eat(name):
#     print('%s要开始吃了!'%(name))
#     while True:
#         food = yield food
#         print('%s 在吃%s' %(name,food))
# user = eat('alex')
# print(user.__next__())
# # print(user.send('泔水'))
#
# user.send('包子')
# user.send('饺子')


# def eat(name):
#     print('%s要开始吃了！' % name)
#     while 1:
#         food = yield
#         print('{}在吃{}'.format(name, food))
#
# a = eat('alex')
# a.__next__()
# # a.send('包子')






a = ((x * 2for x in range(1,101)))
print(sum(a))
b = [x * 2for x in range(1,101) ]
