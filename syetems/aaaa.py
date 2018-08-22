#!/usr/bin/python
# -*- coding: utf-8 -*-
flag = True
while flag:
    guess_num = input('请输入你要猜的数字,退出按q:')
    if guess_num.isdigit():
        guess_num = int(guess_num)
        if guess_num >= 90:
            print('再见了,这个时间')
        elif guess_num >= 70:
            print('人生快结束了')
        elif guess_num >= 60:
            print('还不错的老屁孩')
        elif guess_num >= 50:
            print('即将变成不听话的老屁孩')
        elif guess_num >= 40:
            print('差不多写到这了')
        else:
            print('人生黄金年龄')
    else:
        if guess_num == "q" or guess_num == "Q":
            pass
            exit(8)
        else:
            print('请输入数字')