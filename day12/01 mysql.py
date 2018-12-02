#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import pymysql
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='123',
    database='abc',
    charset='utf8'
)

username = input('请输入用户名：').strip()
password = input('请输入密码：').strip()

cursor = conn.cursor()
sql = "select * from userinfo where user=%s and password=%s;"

ret = cursor.execute(sql,[username,password])
print(ret)

if ret:
    print('登录成功')
else:
    print('登录失败')