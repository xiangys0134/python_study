#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import socket

client = socket.socket()
client.connect(('127.0.0.1',8001))

while True:
    msg = input('请输入>>>：').strip()
    client.send(msg.encode())
    ret_msg = client.recv(1024)
    print(ret_msg.decode())

