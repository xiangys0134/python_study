#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import socket

client = socket.socket()

client.connect(('127.0.0.1',8000))

msg = input('>>>:').strip()

client.send(msg.encode('utf8'))

msg = client.recv(1024)
print('对方回复：',msg)

client.close()