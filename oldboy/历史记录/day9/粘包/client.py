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
    # print('##############',ret)
    if not ret:
        continue
    if ret != 'q':
        client.send(ret.encode('utf8'))
        total_bytes = client.recv(1024)
        total_size = int(total_bytes.decode())
        print(total_size,'############')
        client.send('read_ok'.encode('utf8'))
        # if total_size<1024:
        comomd = client.recv(total_size)
        print(comomd.decode('gbk'))
        # else:


