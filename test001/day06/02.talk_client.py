#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket


sock = socket.socket()

sock.connect(('127.0.0.1',8800))

data = sock.recv(1024)
print("recv data:",data.decode('utf-8'))
while True:
    inp = input('>>>')
    # print('xxxxxxxxxxxxxxxxxxxxxx')
    sock.sendall(inp.encode('utf-8'))
    if inp == 'q' or inp == 'Q':
        break
    if len(inp) == 0:
        print('0字节')
        break
    data = sock.recv(1024)
    print("recv data:", data.decode('utf-8'))

sock.close()


