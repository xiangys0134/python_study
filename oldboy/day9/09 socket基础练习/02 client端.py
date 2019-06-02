#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

sk = socket.socket()
sk.connect(('127.0.0.1',8800))
sk.send(b'hello world!')
ret = sk.recv(1024)

print(ret)

sk.close()

