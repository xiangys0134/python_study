#!/usr/bin/python
# -*- coding: utf-8 -*-

# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return abs(x)
#
# print(my_abs(-126))

# import math
#
# def move(x,y,step,*args,angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx,ny
#
# a = move(4,5,6,angle=3)
# print(a)


# def power(x):
#     return x * x
# print(power(5))

#
# def calc(*args):
#     return args
#
# l1 = [1,2,3,4,5,6,7,8]
# #a = calc(1,2,3,4,5,6)
# a = calc(*l1)
#
# print(a)


# def person(name,age,**kwargs):
#     print(name,age,kwargs)
#
# dict1 = {'好友':'李四','job':'IT'}
# #person('张三',21,d=5,你好='中国')
# person('张三',21,**dict1)



def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
    #n * fact(n-1) = 10 * fact(9) = 10 * 9 * fact(8) = 10 * 9 * 8 * fact(7) =10 * 9 * 8 * 7 * fact(6) \
    #= 10 * 9 * 8 * 7 * 6 * fact(5) =10 * 9 * 8 * 7 * 6 * 5 * fact(4) =10 * 9 * 8 * 7 * 6 * 5 * 4 * fact(3) \
    #=10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * fact(2) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * fact(1) = 10 * 9 * 8 * 7 * 6 * 5 \
    #* 4 * 3 * 2 * 1 = 3628800

a = fact(10)
print(a)

