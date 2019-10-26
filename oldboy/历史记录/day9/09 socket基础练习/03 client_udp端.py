#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

udp_sk = socket.socket(type=socket.SOCK_DGRAM)
udp_sk.sendto(b'hello mi!',('127.0.0.1',8801))
ret = udp_sk.recvfrom(1024)

print(ret)

udp_sk.close()
