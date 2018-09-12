#!/usr/bin/env python
# -*- coding:utf-8 -*-
#yousong.xiang
#模拟博客园登陆
#v1.0.1

import time

l1 = ['请登录','请注册','文章页面','日记页面','评论页面','收藏页面','注销','退出程序']
user_db = 'register'    #用户信息表
tb1 = []    #将登陆信息作为session存储到字典中
c_time = time.time()

#登录检测装饰器
def login_check(func):
    '''登录检测函数'''
    def inner(*args,**kwargs):
        print(tb1)
        if tb1 == False:
            ret = func(*args,**kwargs)
            return ret
    return inner


#登陆函数
@login_check
def login(user,password):
    with open(user_db,'r',encoding='utf-8') as f:
        for i in f:
            register_u = i.split(',')[0].strip()
            print(register_u)
            register_p = i.split(',')[1].strip()
            print(register_p)
            if str(user).strip().lower() == register_u.lower() and str(password).strip() == register_p:
                #tb1[str(user).strip()] = c_time
                tb1.append(str(user).strip())
                return 1
            else:
                return 0
            # else:
            #     return 2


#注册函数
def register(user,password):
    with open(user_db,'r',encoding='utf-8') as f:
        for i in f:
            if str(user).strip().lower() == i.lower():
                return 0

    with open(user_db,'a',encoding='utf-8') as f1:
        f1.write(str(user).strip() + ',' + str(password).strip() + '\n')
        #tb1[str(user).strip()] = c_time
        l2.append(str(user).strip())
        return 1




#装饰器 作为语句执行时用户是否登陆检查
def wrapper_login(func):
    def inner(*args,**kwargs):
        if l1:
            ret = func(*args,**kwargs)
            return ret
        else:
            print('请先登录!!!')
    return inner

#装饰器 日志打印
def wrapper_logs(func):
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        return ret
    return inner

#文字页面函数
def article():
    print('我查看文字啦')


#日记页面函数

def diary():
    print('我写日记啦')

#评论函数
def comment():
    print('我要评论啦')

#收藏函数
def collection():
    print('我要收藏啦')

#注销函数
def logout():
    print('我要注销啦')


flag = True

while flag:
    for i in range(len(l1)):
        print('序号['+ str(i) + ']' + ': ' + l1[i])
    seve_id = input('请输入：')
    if seve_id.isdigit() == False:
        print('\033[1;35m序号输入错误!!!\033[0m')
        continue
    else:
        if int(seve_id)>len(l1) or int(seve_id) < 0:
            print('\033[1;35m序号范围异常!!!\033[0m')
            continue

    if seve_id == '0':  #登陆序号
        i = 1
        while i <=3:
            user = input('请输入你的用户:')
            password = input('请输入你的密码:')
            ret = login(user,password)
            if ret == 0:
                if i == 3:
                    print('\033[1;35m账号密码输错超过三次\033[0m')
                else:
                    print('账号或密码登录失败')
                i += 1
            elif ret == 1:
                print('登录成功,欢迎你%s'%(l1[0]))
                break
            elif ret == 2:
                print('用户已经登录,无需再次登录')
                i = 4
            else:
                if i == 3:
                    print('\033[1;35m登录次数超过三次\033[0m')
                else:
                    print('登录失败')
                i += 1

    elif seve_id == '1':    #注册序号
        l2 = []
        user = input('请输入注册用户名:')
        password = input('请输入密码:')
        ret = register(user,password)
        if ret == 0:
            print('该用户已注册,请重新注册')
        elif ret ==1:
            print('用户%s注册成功'%(l2[0]))
        else:
            print('注册用户异常')







