#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

class Auth:
    def __init__(self,user,pwd):
        self.user = user
        self.pwd = pwd

    def login(self):
        client = socket.socket()
        client.connect(('127.0.0.1',8000))
        client.send(self.user.encode('utf8'))
        msg = client.recv(1024)
        if msg.decode('utf8') == 'user_auth':
            client.send(self.pwd.encode('utf8'))
            msg = client.recv(1024)
            return msg.decode('utf8')

    def register(self):
        pass