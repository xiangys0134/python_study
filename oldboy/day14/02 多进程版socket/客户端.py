#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

client = socket.socket()
client.connect(('127.0.0.1',8801))

while True:
    msg = input('>>>:').strip()
    if not msg:continue

    client.send(msg.encode('utf8'))
    data = client.recv(1024)
    print(data.decode('utf8'))