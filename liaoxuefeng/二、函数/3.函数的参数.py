#!/usr/bin/env python
# -*- coding:utf-8 -*-

# def power(x):
#     return x * x
#
# da = power(5)
# print(da)

# def power(x,n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s *  x
#     return s
# dc = power(3,2)
# print(dc)


# def emroll(name,gender,age=6,city='Beijing'):
#     print('name:',name)
#     print('gender:',gender)
#     print('age:',age)
#     print('city:',city)
#
# print(emroll('张三','男'))


def emroll(a,b,*args,**kwargs):
    return a,b,args,kwargs


l1 = [1,2,3,4]
ds = emroll('张三',98,'ccc','dddd',*l1,city='4')
print(ds)





