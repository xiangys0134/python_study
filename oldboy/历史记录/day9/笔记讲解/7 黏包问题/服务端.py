# -*- coding: utf-8 -*-
"""
基于TCP的socket会出现黏包问题
服务端
"""

import socket

server = socket.socket()
server.bind(('127.0.0.1', 8091))

server.listen(5)


conn, addr = server.accept()
msg1 = conn.recv(1024)
print('第一次收到：', msg1)
msg2 = conn.recv(4)
print('第二次收到：', msg2)
msg3 = conn.recv(5)
print('第三次收到：', msg3)
conn.close()
server.close()