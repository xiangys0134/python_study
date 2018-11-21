#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

class Myclient:
    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(('127.0.0.1',8000))

    def mysend(self,dic):
        self.sk.send(dic.encode('utf8'))
        # msg = self.sk.recv(1024)
        # print(msg.decode('utf8'))

    def myrecv(self):
        msg = self.sk.recv(1024)
        # print(msg)
        return msg


# t1 = {'username':'alex','pwd':'123','job':'user'}
t1 = 'aaa'
myclient = Myclient()
myclient.mysend(t1)
msg = myclient.myrecv()
print(msg)
