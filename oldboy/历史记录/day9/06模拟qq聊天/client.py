#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
udp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

qq_name_dic={
    '金老板':('127.0.0.1',8002),
    '哪吒':('127.0.0.1',8002),
    'egg':('127.0.0.1',8002),
    'yuan':('127.0.0.1',8002),
}

while True:
    qq_name = input('请选择聊天对象:').strip()
    while True:
        msg = input('请输入消息，回车发送，输入q结束和ta的聊天：').strip()
        if msg == 'q':
            break
        if not msg or not qq_name or qq_name not in qq_name_dic:
            continue

        udp_client_socket.sendto(msg.encode('utf8'),qq_name_dic[qq_name])

        back_msg,addr = udp_client_socket.recvfrom(1024)
        print(back_msg.decode('utf8'))
        print('来自[%s:%s]的一条消息:%s'%(addr[0],addr[1],back_msg.decode('utf8')))
        print('\n')


udp_client_socket.close()
