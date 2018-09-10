#!/usr/bin/env python
# -*- coding:utf-8 -*-
#yousong.xiang
#模拟博客园登陆
#v1.0.1

import time

user_db = 'register'    #用户信息表
tb1 = {}    #将登陆信息作为session存储到字典中
c_time = time.time()
#登陆函数
def login(user,password):
    with open(user_db,'r',encoding='utf-8') as f:
        for i in f:
            if str(user).strip().lower() == i.lower() and str(password).strip().lower() == i.lower():
                tb1[str(user).strip()] = c_time
                return 1,tb1
        return 0


#注册函数
def register(user,password):
    with open(user_db,'r',encoding='utf-8') as f:
        for i in f:
            if str(user).strip().lower() == i.lower():
                return 0

    with open(user_db,'a',encoding='utf-8') as f1:
        f1.write(str(user).strip() + ',' + str(password).strip() + '\n')
        tb1[str(user).strip()] = c_time
        return 1,tb1

#装饰器 作为语句执行时用户是否登陆检查
def wrapper_login(func):
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        return ret
    return inner

def wrapper_logs(func):
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        return ret
    return inner

