#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket


sock = socket.socket()

sock.connect(('127.0.0.1',8800))

data = sock.recv(1024)
print("recv data:",data.decode('utf-8'))

while True:
    cmd = input('>>>')
    sock.sendall(cmd.encode('utf-8'))
    if cmd == 'q' or cmd == 'Q':
        break
    if len(cmd) == 0:
        print('0字节')
        break

    import struct
    header = sock.recv(4)
    respones_length = struct.unpack("i",header)[0]

    data = sock.recv(respones_length)

    import json
    data_length = json.loads(data.decode('utf-8'))["data_length"]

    respones_length = sock.recv(data_length)
    print("recv data:", respones_length.decode('gbk'))

sock.close()




