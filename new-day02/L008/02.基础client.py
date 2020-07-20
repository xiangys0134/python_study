#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sock = socket.socket()

sock.connect(("127.0.0.1",8800))


sock.send('hello word!'.encode("utf-8"))
data = sock.recv(1024)

print(data.decode("utf-8"))