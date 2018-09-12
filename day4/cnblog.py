#!/usr/bin/env python
# -*- coding:utf-8 -*-
#yousong.xiang 2018.9.12
#模拟博客园登陆
#v1.0.1
#功能介绍：
#1.文件存放在register目录中，用户注册通过该文件进行判断用户是否已存在
#2.通过列表tb1将用户的登录信息存放至该列表中，默认环境为单用户登陆环境，列表只保存了一个session值
#通过用户交互输入0-7数字后if判断调用对应的函数
#在调用相关函数后会将日志写入accesslog.log中，日志格式：2018-09-12 19:37:05 调用函数logout 返回值:1
#https://github.com/xiangys0134/job/blob/master/day4/cnblog.py

import time

l1 = ['请登录','请注册','文章页面','日记页面','评论页面','收藏页面','注销','退出程序']
user_db = 'register'    #用户信息表
tb1 = []    #将登陆信息作为session存储到字典中
c_time = time.time()
log = 'accesslog.log'

#登录检测装饰器
def login_check(func):
    '''登录检测函数,如果用户已经登录则将用户session写入列表tb1中,不为空则跳出登录验证'''
    def inner(*args,**kwargs):
        print(tb1)
        if tb1 == []:
            #print(tb1)
            #print('aaaa')
            ret = func(*args,**kwargs)
            return ret
        else:
            #print('已登录,无需再次登录11')
            #print(tb1)
            return 2
    return inner


#登陆函数
@login_check
def login(user,password):
    with open(user_db,'r',encoding='utf-8') as f:
        for i in f:
            register_u = i.split(',')[0].strip()
            #print(register_u)
            register_p = i.split(',')[1].strip()
            #print(register_p)
            if str(user).strip().lower() == register_u.lower() and str(password).strip() == register_p:
                #tb1[str(user).strip()] = c_time
                tb1.append(str(user).strip())
                return 1
        else:
            return 0

            # else:
            #     return 2


#注册函数
@login_check    #判断用户是否已经登录,如果已经登录则不能进行注册
def register(user,password):
    with open(user_db,'r',encoding='utf-8') as f:
        for i in f:
            if str(user).strip().lower() == i.lower():
                return 0

    with open(user_db,'a',encoding='utf-8') as f1:
        f1.write(str(user).strip() + ',' + str(password).strip() + '\n')
        #tb1[str(user).strip()] = c_time
        tb1.append(str(user).strip())
        return 1




#装饰器 作为语句执行时用户是否登陆检查
def wrapper_login(func):
    '''判断用户提交时是否先处于登录状态'''
    def inner(*args,**kwargs):
        if tb1:
            ret = func(*args,**kwargs)
            # print(tb1)
            # print('tb1不为空')
            return ret
        else:
            print('请先登录!!!')
    return inner

#装饰器 日志打印
def wrapper_logs(func):
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        logs_time = time.strftime('%Y-%m-%d %H:%M:%S')
        names = func.__name__
        print('我调用了%s函数'%names)
        with open(log,'a',encoding='utf-8') as f:
            f.write('\n%s 调用函数%s 返回值:%s'%(logs_time,names,ret))
        return ret
    return inner

#文字页面函数
@wrapper_login
@wrapper_logs
def article():
    print('我查看文字啦')


#日记页面函数
@wrapper_login
@wrapper_logs
def diary():
    print('我写日记啦')

#评论函数
@wrapper_login
@wrapper_logs
def comment():
    print('我要评论啦')

#收藏函数
@wrapper_login
@wrapper_logs
def collection():
    print('我要收藏啦')

#注销函数
@wrapper_login
@wrapper_logs
def logout(*args):
    print(args)
    #args = str(args)
    print('用户:%s注销成功'%(args))
    return 1


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
                print('登录成功,欢迎你%s'%(tb1[0]))
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
        elif ret == 1:
            print('用户%s注册成功'%(tb1[0]))
        elif ret == 2:
            print('用户已经处于登录状态,无法再进行注册')
        else:
            print('注册用户异常')

    elif seve_id == '2':    #文章页面
        article()

    elif seve_id == '3':    #日记页面
        diary()

    elif seve_id == '4':    #评论页面
        comment()

    elif seve_id == '5':    #页面收藏
        collection()

    elif seve_id == '6':    #注销程序
        ret = logout(*tb1)
        if ret == 1:
            tb1 = []
    elif seve_id == '7':    #退出程序
        print('程序退出...')
        exit(5)
