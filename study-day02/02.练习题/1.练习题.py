#!/user/bin/env python3
# -*- coding: utf-8 -*-

#name = input(“>>>”) name变量是什么数据类型
#通过input函数获取的值都为字符串类型

s1 ='''
文能提笔安天下,  
武能上马定乾坤.  
心存谋略何人胜,  
古今英雄唯是君.
'''

# print(s1)


name = '麻花藤'

# s1 = input("请输入用户名：")
#
# if s1 == name:
#     print('答对了')
# else:
#     print('傻逼')

# s = 0
# while s <= 10:
#     count_a = s + 1
#     s += 1
#     print(count_a)

# count_int = 0
# for i in range(1,101):
#     count_int += i
#     # print(i)
#
# print(count_int)

# count_int = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         count_int += i
#
# print(count_int)

count_a = 0
for i in range(1,101):
    if i % 2 == 0:
        i = -i
    count_a += i
print(count_a)





