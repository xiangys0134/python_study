#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

ip_port = ('127.0.0.1',8000)
udp_server_socket = socket.socket(socket.AF_INET,type=socket.SOCK_DGRAM)
udp_server_socket.bind(ip_port)

while True:
    qq_msg,addr = udp_server_socket.recvfrom(1024)
    print('来自[%s]的一条信息：%s' %(addr,qq_msg.decode('utf8')))
    back_msg = input('回复消息：').strip()

    if not back_msg:
        continue

    udp_server_socket.sendto(back_msg.encode('utf8'),addr)
