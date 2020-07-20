#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

# def my_func():
#     time.sleep(2)
#     print("编写了一段程序")
#
# print(time.time())
# my_func()
# print(time.time())
#
#


# def wrapper(func):
#     def inner(*args,**kwargs):
#         print("装饰器之前")
#         ret = func(*args,**kwargs)  #执行被装饰的函数 得到返回值ret
#         print("装饰器之后")
#         return ret  # 被装饰函数的返回值返回
#     return inner
#
# @wrapper
# def func(a,b,c):
#     print("我是被装饰的函数 %s %s %s"%(a,b,c))
#
# ret = func(1,2,3)
#
#
# def wraooer(func):
#     def inner(*args,**kwargs):
#         ret = func(*args,**kwargs)
#         return ret
#     return inner



# 登陆验证
login_user =False
def login(func):
    def inner(*args,**kwargs):
        global login_user
        if not login_user:
            username = input('username：')
            password = input('password：')
            if username == 'alex' and password == '123':
                login_user = True
                ret = func(*args, **kwargs)
                return ret
        if login_user:
            ret = func(*args, **kwargs)
            return ret
    return inner

@login
def select():
    print('查询数据')

@login
def delete():
    print('删除数据')

@login
def set():
    print('修改数据')

s1  = set()
print(s1)

s2 = delete()
print(s2)


# 日志记录






