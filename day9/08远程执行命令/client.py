#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

client = socket.socket()
client.connect(('127.0.0.1',8004))
while True:
    msg = input('输入需要发送的消息：').strip()
    client.send(msg.encode('utf8'))
    back_msg = client.recv(1024)
    print(back_msg.decode('gbk'))

client.close()