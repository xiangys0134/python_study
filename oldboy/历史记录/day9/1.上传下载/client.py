#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket,subprocess
client = socket.socket()
client.connect(('127.0.0.1',8000))
# msg = input('请输入你的信息>>>:').strip()
msg = 1
while msg != 'q':
    msg = input('请输入你的信息>>>:').strip()
    if not msg:
        print('信息为空,请重新输入')
        continue
    client.send(msg.encode('utf8'))
    #2.服务端发送长度
    total_len = client.recv(1024)
    #3.开启seq认证
    is_ready = b"RECV_OK"
    client.send(is_ready)
    #4.接收服务端发送过来的数据
    reve_data = b''
    recv_size = 0

    print(total_len.decode('utf8'),type(total_len))

    if int(total_len.decode('utf8')) <= 1024:
        reve_data = client.recv(int(total_len.decode('utf8')))
    else:
        while recv_size < int(total_len.decode('utf8')):
            data = client.recv(1024)
            reve_data += data
            recv_size += len(data)
    recv_msg = reve_data.decode('gbk')

    print('收到发送过来的消息：%s'%(recv_msg))



