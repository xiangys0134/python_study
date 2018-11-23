# -*- coding: utf-8 -*-

"""
循环获取用户输入
"""

import socket

# 买手机
client = socket.socket()

# 连接服务端
client.connect(('127.0.0.1', 8000))

while 1:
    # 发数据
    msg = input('>>>>:').strip()
    client.send(msg.encode('utf8'))  # 给服务端发消息
    # 收数据
    msg = client.recv(1024)
    print('对方回复：', msg.decode('utf8'))


# 挂了
client.close()