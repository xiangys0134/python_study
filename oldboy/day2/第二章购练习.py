#!/usr/bin/env python
# -*- coding:utf-8 -*-

a ={
        '1':['电脑',1999],
        '2':['鼠标',10],
        '3':['袜子',15],
        '4':['衬衫',108],
        'n':'购物车结算'
    }

#商品列表函数
def goods_list():
    #print('商品选择:')
    for k,y in a.items():
        if k != 'n':
            print('序号:%s \t  商品型号：%s \t 商品价格：%s'%(k,a[k][0],a[k][1]))
    else:
        print('序号:n \t\t %s'%a['n'])


#用户充值,传入参数对充值金额进行判断
def char_money(mon):
    if mon <= 0:
        return 1
    else:
        #print('请输入正确金额')
        return 0

#用户充值
flag = True
while flag:
    mon = input('请输入需要充值的金额:')
    if mon.isdigit():
        mon = int(mon)
    else:
        print('请输入正确值')
        continue
    #对金额进行判断
    result = char_money(mon)
    #char_money返回值 0：充值成功 1:充值为负数
    if result == 0:
        print('充值成功,充值金额为:%s'%mon)
        flag = False
    elif result == 1:
        print('填写的值为负数,错误')
    else:
        print('充值失败,请重新充值!!!')

l1 = []
l2 = []
tb1 = {}
#商品换算
def goods_select(goods,mon):
    mon -= a[goods][1]
    return mon
flag = True
while flag:
    print('选择你要购买的商品:')
    goods_list()
    goods = input('请输入你要购买的商品序号:')
    if goods == 'n':
        if l1:
            print('购买商品:','单价:')
            #print(l1,l2)
            for i in range(len(l1)):
                print(str(l1[i]) + '\t'+ '\t'+str(l2[i]))
        print('余额为%s'%mon)
        flag = False
    elif goods in a:
        c = goods_select(goods,mon)
        if c >= 0:
            mon = goods_select(goods, mon)
            x = a[goods][0]
            y = a[goods][1]
            #l1表示商品类型 l2表示商品价格
            l1.append(x)
            l2.append(y)
            #单以购买的商品信息写入字典存在bug
            #tb1 = {}
            print('-----------------------')
            print('购买商品:%s \t 单价:%s \t 余额:%s'%(x,y,mon))
        else:
            print('购买余额不足,当前余额%s'%mon)
    else:
        print('输入错误')

