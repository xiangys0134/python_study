#!/usr/bin/env python
# -*- coding:utf-8 -*-
#yousong.xiang 2018.9.4
#v1.0.2
#修改字典参数，添加对应的备注，修复bug，友好打印
#预先需要两个文件 users.txt、session

import os
#商品字典
a ={
        '1':['电脑',1999],
        '2':['鼠标',10],
        '3':['袜子',15],
        '4':['衬衫',108]
       # 'n':'购物车结算'
    }


select_user = ['登录','注册','购物','退出']
#用户信息保存文件,文件存储格式 'user password'
users_file = 'users.txt'    #用户账号密码文件
session_file = 'session'    #session文件包含用户登录信息

def loggin(user,password):  #用户登陆函数
    with open(users_file,encoding='utf-8') as f_user:
        for i in f_user:
            if i == '':
                continue
            user_info = i.split()
            if user == user_info[0] and password == user_info[1]:
                return 1

def register(user,password):    #0 表示用户已存在 1表示用户注册成功 2表示用户注册时不能使用特殊字符
    with open(users_file,encoding='utf-8') as f_user:
        for i in f_user:
            user_info = i.split()
            if user == user_info[0]:    #判断用户是否存在,存在则返回0
                return 0
    if str(user).isalnum() == False or str(password).isalnum() == False:    #账号密码不能为特殊字符
        return 2

    with open(users_file,'a',encoding='utf-8') as f_user:
        f_user.write(user + '\t' + password +'\n')
        return 1



#商品列表函数，该函数主要用来打印商品列表
def goods_list():
    print('\033[0;31;46m商品列表\033[0m')  #打印对应商品
    for k,y in a.items():
        print('序号:%s \t  商品型号：%s \t 商品价格：%s'%(k,a[k][0],a[k][1]))
    #print('序号:n \t\t %s'%a['n'])



#商品消费余额、结算判断,判断机制：函数返回3个值，分别是商品、价格、余额.同时将商品写入字典或者文件中 tb1设计字样{'电脑':2} //2表示购买数量
tb1 = {}
l1 = []
left_money = 0
#购买商品运算函数,传参商品序号及余额,将每次的余额写入到一个列表中,最终结算时取-1索引值 goods_id表示读取商品字典的序号
def goods_select(goods_id):
    #购买商品判断,对购买商品的余额进行判断,如果列表为空则将第一次传参的金额写入到列表l1中作为余额使用,以下处理逻辑不好,先对列表进行判断是否为空,在运算是否满足购买
    if l1:
        #print(l1[-1])
        #如果余额大于则进行运算
        if l1[-1] >= a[goods_id][1]:
            remain = l1[-1] - a[goods_id][1]
            l1.append(remain)
            #对商品进行判断并写入字典中,如果商品已经存在字典中则对商品数量进行相加处理tb1 = {'电脑':2,'鼠标':1},另外返回数字1表示购买成功,购买成功则return l1,tb1,1  反之则return l1,tb1,0
            shopping_names = a[goods_id][0]
            print(shopping_names)
            if shopping_names in tb1:
                tb1[shopping_names] += 1
                # return l1,tb1,1
            else:
                tb1[shopping_names] = 1
                #将余额列表l1,购买商品字典tb1做return返回,用于显示
            return 1
        else:
            return 0

    else:
        #l1[0] = mon
        l1.append(mon)
        if l1[-1] >= a[goods_id][1]:
            remain = l1[-1] - a[goods_id][1]
            l1.append(remain)
            #对商品进行判断并写入字典中,如果商品已经存在字典中则对商品数量进行相加处理tb1 = {'电脑':2,'鼠标':1},另外返回数字1表示购买成功
            shopping_names = a[goods_id][0]
            if shopping_names in tb1:
                tb1[shopping_names] += 1
                # return l1,tb1,1
            else:
                tb1[shopping_names] = 1
                #将余额列表l1,购买商品字典tb1做return返回,用于显示
            return 1
        else:
            return 0

# flag = True

# def shopping():
    #用户充值,与用户进行交互输入金额，如非数字则重新输入，注意：充值只能充值整数
# flag = True
# while flag:
#     mon = input('请输入需要充值的金额:')
#     #对金额进行判断
#     if mon.isdigit() == False:
#         print('输入值有误,请重新输入!!!')
#         continue
#     #result = char_money(mon)
#     # if result == 0:
#     print('充值成功,充值金额为:%s'%mon)
#     mon = int(mon)
#     flag = False


#商品购买,通过循环与用户进行交互
# flag = True
# while flag:
#     goods_list()
#     #mon = int(mon)
#     goods = input('请输入你要购买的商品序号,退出按键[n|N]:')
#     #判断如果用户退出则进行换算
#     if goods == 'n' or goods == 'N':
#         ##退出时判断是否之前有过购买记录,有则打印
#         if tb1:
#             print('\033[32;0m你购买的商品如下:\033[0m')
#             for k, v in tb1.items():
#                 print('商品：%s  数量：%s' % (k, v))
#             print('余额：\033[1;35m %s \033[0m' % (l1[-1]))
#         else:
#             #若为购买商品则直接打印充值金额mon
#             print('未购买商品 余额：\033[1;35m %s \033[0m' % (mon))
#         #flag = False
#         break
#
#     #商品购买机制判断选项如果是非n或者是数字,其实只需要判断是数字即可
#     if not goods.isdigit() or goods not in a:
#         print('\033[1;35m 选择错误,请重新选择!\033[0m')
#         print('\n\n')
#         continue
#
#     #用户正常进行购物车选择商品
#     a1 = goods_select(goods)
#     if a1 == 1:
#         print('\033[1;32m购物车：\033[0m')
#         for k, v in tb1.items():
#             print('商品：%s  数量：%s' % (k, v))
#         print('\033[0;31m余额：%s \033[0m' % (l1[-1]))
#         print('\n')
#     else:
#         print('商品：\033[0;31m%s\033[0m无法进行购买,余额：\033[0;31m %s \033[0m' % (a[goods][0], l1[-1]))

flag = True
count = 1
while flag:
    for i in range(len(select_user)):
        print('序号' + '[' + str(i) + ']' + ' ' + select_user[i])
    client_select_id = input('请输入你的选项:')
    if client_select_id.isdigit():
        if len(select_user) >= int(client_select_id) >= 0:
            # if os.path.exists(session_file):    #情况session用户登录状态
            #     os.remove(session_file)

            if int(client_select_id) == 0:   #如果用户选择登录选项则执行以下操作
                count = 1
                while count <= 3:
                    user = input('请输入你的账号：')
                    password = input('请输入你的密码：')
                    #对用户进行判断
                    result = loggin(user,password)
                    if result == 1:
                        print('用户登录成功')
                        if os.path.exists(session_file):    #情况session用户登录状态
                            os.remove(session_file)
                        with open(session_file,'w',encoding='utf-8') as f1:
                            f1.write(user)
                        flag = False
                        break
                    else:
                        print('用户登录失败,请重新登录')
                        count += 1
                        if count >3:
                            print('登录次数超过3次')

            #tb1 = {}
            if int(client_select_id) == 1:   #用户注册
                fix = True
                while fix:
                    user = input('注册账号：')
                    password = input('注册密码：')
                    result = register(user,password)
                    if result == 0:
                        print('用户已存在')
                    elif result == 2:
                        print('请使用字母大小写及数字')
                    elif result == 1:
                        print('用户注册成功')
                        if os.path.exists(session_file):    #情况session用户登录状态
                            os.remove(session_file)
                        with open(session_file,'w',encoding='utf-8') as f1:
                            f1.write(user)
                        fix = False
                    else:
                        pass

            if int(client_select_id) == 2:  #用户购物
                if os.path.exists(session_file) == False:
                    print('请先登录')

                with open(session_file,'r',encoding='utf-8') as f2: #读取用户session
                    file_session = f2.read()
                    if file_session:
                        ##用户进行充值
                        flag = True
                        while flag:
                            mon = input('请输入需要充值的金额:')
                            # 对金额进行判断
                            if mon.isdigit() == False:
                                print('输入值有误,请重新输入!!!')
                                continue
                            # result = char_money(mon)
                            # if result == 0:
                            print('充值成功,充值金额为:%s' % mon)
                            mon = int(mon)
                            flag = False

                        #用户进行购买
                        # 商品购买,通过循环与用户进行交互
                        flag = True
                        while flag:
                            goods_list()
                            # mon = int(mon)
                            goods = input('请输入你要购买的商品序号,退出按键[n|N]:')
                            # 判断如果用户退出则进行换算
                            if goods == 'n' or goods == 'N':
                                ##退出时判断是否之前有过购买记录,有则打印
                                if tb1:
                                    with open(session_file,'r',encoding='utf-8') as f1:
                                        f1 = f1.readline()[0]
                                    print('\033[32;0m用户:%s 你购买的商品如下:\033[0m'%(f1))
                                    for k, v in tb1.items():
                                        print('商品：%s  数量：%s' % (k, v))
                                    print('余额：\033[1;35m %s \033[0m' % (l1[-1]))
                                else:
                                    # 若为购买商品则直接打印充值金额mon
                                    print('未购买商品 余额：\033[1;35m %s \033[0m' % (mon))
                                # flag = False
                                break

                            # 商品购买机制判断选项如果是非n或者是数字,其实只需要判断是数字即可
                            if not goods.isdigit() or goods not in a:
                                print('\033[1;35m 选择错误,请重新选择!\033[0m')
                                print('\n\n')
                                continue

                                # 用户正常进行购物车选择商品
                            a1 = goods_select(goods)
                            if a1 == 1:
                                print('\033[1;32m购物车：\033[0m')
                                for k, v in tb1.items():
                                    print('商品：%s  数量：%s' % (k, v))
                                print('\033[0;31m余额：%s \033[0m' % (l1[-1]))
                                print('\n')
                            else:
                                print('商品：\033[0;31m%s\033[0m无法进行购买,余额：\033[0;31m %s \033[0m' % (a[goods][0], l1[-1]))

                #无法通过seesion功能将注册或登录的用户进行
                    else:
                        print('用户未登录,请返回进行登录')

            if int(client_select_id) == 3:  #退出
                print('退出')
                break





# if (int(id) -1) == 0:    #用户进行登陆
#     pass





