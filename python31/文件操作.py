#!/user/bin/env python3
# -*- coding: utf-8 -*-

f = open('userinfo',encoding='utf-8')
# print(f.readline())
# print('###########')
# for i in f.read().split('\n'):
#     print(i)
for i in f:
    print(i.strip())
f.close()