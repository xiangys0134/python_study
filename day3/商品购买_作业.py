#!/usr/bin/env python
# -*- coding:utf-8 -*-
#yousong.xiang 2018.9.3
#v1.0.1
#修改字典参数，添加对应的备注，修复bug，友好打印
#
#商品字典
a ={
        '1':['电脑',1999],
        '2':['鼠标',10],
        '3':['袜子',15],
        '4':['衬衫',108]
       # 'n':'购物车结算'
    }

#商品列表函数，该函数主要用来打印商品列表
def goods_list():
    print('商品列表-------效果展示太low--------')  #打印对应商品
    for k,y in a.items():
    #     if k != 'n':
        print('序号:%s \t  商品型号：%s \t 商品价格：%s'%(k,a[k][0],a[k][1]))
    #print('序号:n \t\t %s'%a['n'])

#用户充值,传入参数对充值金额进行判断
# def char_money(mon):
#     if mon:
#         mon = int(mon)
#         #left_money = mon
#         if mon <= 0:
#             print('充值金额不能为负数')
#             return 3
#         else:
#             return 0
#     else:
#         print('请输入正确金额')
#         return 2

#商品消费余额、结算判断,判断机制：函数返回3个值，分别是商品、价格、余额.同时将商品写入字典中
tb1 = {}
l1 = []
left_money = 0
#传参商品及余额
def goods_select(goods,mon):
    mon -= a[goods][1]

    #print(mon)
    #print(a[goods][0])
    if goods == 'n':
        #print('即将进行结算') 3表示即将进行结算
        return 3
    elif goods in a:
        if mon >= 0:
            #将商品名和价格存入字典中
            k = a[goods][0]
            y = a[goods][1]
            #print(k,y)
            tb1[k] = y
            l1.append(y)
            ##0表示将商品写入到字典中
            return 0
        else:
            #print('余额不足') 1表示用户余额不足
            return 1
    else:
        #print('输入的商品选项有误') 2表示商品选项输入错误
        return 2

#用户充值,与用户进行交互输入金额，如非数字则重新输入，注意：充值只能充值整数
flag = True
while flag:
    mon = input('请输入需要充值的金额:')
    #对金额进行判断
    if mon.isdigit() == False:
        print('输入值有误,请重新输入!!!')
        continue
    #result = char_money(mon)
    # if result == 0:
    print('充值成功,充值金额为:%s'%mon)
    flag = False
    #     mon = int(mon)
    # else:
    #     print('充值失败,请重新充值!!!')

#商品购买,通过循环与用户进行交互
#goods_list()
flag = True
while flag:
    goods_list()
    goods = input('请输入你要购买的商品序号,退出按键[n|N]:')
    if goods != 'n' or goods != 'N':
        #将余额mon转换为数字型
        mon = int(mon)
        a = goods_select(goods,mon)
    print(a)
    # 0：购买成功 1：余额不足 2：输入的序号不正确 3：结算
    if a == 2:
        print('输入的商品选项有误,请重新输入')
        continue
    if a == 1:
        print('余额不足')
        flag = False
    if a == 0:
        print('商品购买成功')
        flag = False
    if a == 3:
        print('进行结算')
        if tb1:
            print('共购买商品:%s'%(len(tb1)))
            count = 0
            print(tb1)
            for k,y in tb1.items():
                count += y
                print('商品列表：%s'%(k))
            print('消费金额：%s'%count,'余额：%s'%mon)
        else:
            print('未购买商品,余额为%s'%mon)
        flag = False


