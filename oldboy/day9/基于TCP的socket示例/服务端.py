#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

server = socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(5)
conn,addr = server.accept()

msg = conn.recv(1024)
print(msg.decode('utf8'))

conn.close()
server.close()
