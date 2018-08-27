#!/usr/bin/python
# -*- coding: utf-8 -*-

sen = ['粉嫩','铁锤']
flag = True
str1 = input('请输入你的内容:')


# for i in sen:
#     #print(i)
#     if i in '粉嫩':
#         flag = True
#         while flag:
#             str1 = input('有敏感字符,请重新输入你的内容:')
#             flag = False


while flag:
    for i in sen:
        if i in str1:
            print('有铭感字符')
            break
        else:

print(str1)

# while flag:
#     for i in sen:
#         #print(i)
#         if i in str1:
#             print(i)
#             str1 = input('有敏感字符,请重新输入你的内容:')
#             continue


