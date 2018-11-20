#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
udp_sk = socket.socket(type=socket.SOCK_DGRAM)  #创建一个服务器的套接字
udp_sk.bind(('127.0.0.1',9000))
msg,addr = udp_sk.recvfrom(1024)
print(msg)
print(addr)

udp_sk.sendto(b'hi',addr)
udp_sk.close()
