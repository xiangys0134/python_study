#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

s = socket.socket()
s.connect(('127.0.0.1',9000))

while True:
    msg = input('>>>:').strip()
    if not msg:break

    s.send(msg.encode('utf8'))
    data = s.recv(1024)

    print(data)
