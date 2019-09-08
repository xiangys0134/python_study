#!/usr/bin/python
# -*- coding: utf-8 -*-

# f = open(r'D:\test\test.txt')

# 文件的读操作

# content = f.read()
# print(content)
# for i in f:
#     print(i.strip())
# f.close()

# 写文件
# f = open('write_file',mode='w',encoding='utf-8')
# f.write('你好')

# 图片操作
p1 = open(r'E:\照片\2015涂鸦\DSC_0002.JPG',mode='rb')
content = p1.read()
p1.close()

p2 = open('p1_bak.png','wb')
p2.write(content)
p2.close()

with open('p1_bak2.png',mode='wb') as p1:
    p1.write(content)
