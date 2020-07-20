#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sock = socket.socket()

sock.bind(('127.0.0.1',8800))

sock.listen(5)


conn,addr = sock.accept()

data = conn.recv(1024)
print('data:',data.decode('utf-8'))

