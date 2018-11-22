#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import json
import os


dir = os.path.dirname(os.path.abspath(__name__))
db_dir = os.path.join(dir,'db')
# print(db_dir)

if os.path.exists(os.path.join(db_dir,'user_db')):
    with open(os.path.join(db_dir,'user_db'),'r',encoding='utf8') as f:
        user_dumps = f.read()
        user = json.loads(user_dumps)

if os.path.exists(os.path.join(db_dir,'role_db')):
    with open(os.path.join(db_dir,'role_db'),'r',encoding='utf8') as f1:
        role_dumps = f1.read()
        role = json.loads(role_dumps)

tmp_list = [
    ('登陆','login'),
    ('注册','register'),
    ('退出','exit')
]

# print(len(tmp_list))
class Myclient:
    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(('127.0.0.1',8000))

    def mysend(self,dic):
        self.sk.send(dic.encode('utf8'))


    def myrecv(self):
        msg = self.sk.recv(1024)

        return msg


while True:
    #判断用户是否的行为
    for i in range(len(tmp_list)):
        print(i+1,tmp_list[i][0])
        # print(i)
    info = input('请输入>>>:').strip()

    #如果为用户登陆状态
    if tmp_list[int(info)-1][1] == 'login':
        print('登陆')
        # myclient = Myclient()
        username = input('请输入账号：').strip()
        pwd = input('请输入密码：').strip()
        myclient = Myclient()

        pass
    elif tmp_list[int(info)-1][1] == 'register':
        print('注册')
        pass
    else:
        exit(4)

    # myclient = Myclient()
    # myclient.mysend(user)
    # msg = myclient.myrecv()
    # print(msg)


