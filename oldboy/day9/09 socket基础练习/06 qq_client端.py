#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

udp_client_socket = socket.socket(socket.AF_INET,type=socket.SOCK_DGRAM)
qq_name_dic = {
    '金老板':('127.0.0.1',8000),
    'gold':('127.0.0.1',8000),
    'egg':('127.0.0.1',8000),
    'yuan':('127.0.0.1',8000)
}

while True:
    qq_name = input('输入聊天对象：').strip()
    if not qq_name:
        continue

    if qq_name not in qq_name_dic:continue
    msg = input('请输入聊天内容：').strip()

    if not msg:continue

    udp_client_socket.sendto(msg.encode('utf8'),qq_name_dic[qq_name])
    back_msg,addr = udp_client_socket.recvfrom(1024)
    print('来自[%s]的消息：%s' %(addr[0],back_msg))


