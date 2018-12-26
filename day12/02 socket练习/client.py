#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

client = socket.socket()

client.connect(('127.0.0.1',8081))
client.send(b'hello world .....')
rev_msg = client.recv(1024)
print(rev_msg.decode('utf8'))