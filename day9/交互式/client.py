#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
1.建立socket
2.发送命令
3.接收结果
"""

import socket

client = socket.socket()

client.connect(('127.0.0.1',8090))

while True:
    print('按q键退出')
    ret = input('>>>:').strip()
    if ret != 'q':
        client.send(ret.encode('utf8'))
        comomd = client.recv(1024)
        print(comomd.decode('gbk'))

