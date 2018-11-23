# -*- coding: utf-8 -*-

import socket

# 先要买电话
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket.AF_INET:基于网络的socket  socket.SOCK_STREAM：基于TCP的流式连接
# 插手机卡
phone.bind(('127.0.0.1', 8000))  # 端口：1~65535 ： 1~1024操作系统自用   剩下是应用程序可用的
# 开机
phone.listen(5)

# 等着客户端给我打电话
conn, addr = phone.accept()  # conn:代表连接  addr:对方的地址
while 1:
    # 收消息
    msg = conn.recv(1024)
    # 回消息
    msg_str = msg.decode('utf8')
    answer = '{} sb'.format(msg_str).encode('utf8')
    conn.send(answer)

# 挂电话
conn.close()  # 关闭连接
# 关机
phone.close()  # 关闭服务

