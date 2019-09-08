#!/usr/bin/python
# -*- coding: utf-8 -*-

logined = False
#登陆验证装饰器
def login(func):
    def inner(*args,**kwargs):
        '''登陆逻辑'''
        global logined
        if not logined:
            username = input('username：')
            password = input('password：')
            if username == 'alex' and password == '3714':
                logined = True
        if logined:
            ret = func(*args,**kwargs)
            return ret
    return inner

@login
def select():
    print('要查询数据')

@login
def delete():
    print('要删除数据')

@login
def set():
    print('要修改数据')

select()
set()