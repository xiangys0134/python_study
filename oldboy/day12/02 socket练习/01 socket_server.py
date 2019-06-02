#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

server = socket.socket()
server.bind(('127.0.0.1',8081))
server.listen(3)

while 1:
    conn,addr = server.accept()
    from_browser = conn.recv(1024)
    print(from_browser)
    conn.send(b'hello')

