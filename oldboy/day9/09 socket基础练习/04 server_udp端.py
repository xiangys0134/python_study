#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

udp_sk = socket.socket(type=socket.SOCK_DGRAM)

udp_sk.bind(('127.0.0.1',8801))
msg,addr = udp_sk.recvfrom(1024)
print(msg)

udp_sk.sendto(b'hi',addr)
udp_sk.close()
