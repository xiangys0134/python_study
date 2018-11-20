#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

ip_port = ('127.0.0.1',9000)
udp_sk = socket.socket(type=socket.SOCK_DGRAM)
udp_sk.sendto(b'hello',ip_port)
back_msg,addr = udp_sk.recvfrom(1024)
print(back_msg.decode('utf8'),addr)