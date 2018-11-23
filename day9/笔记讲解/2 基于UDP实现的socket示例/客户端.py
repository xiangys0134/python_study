# -*- coding: utf-8 -*-
"""
UDP客户端
"""

import socket

# 创建一个客户端实例
client = socket.socket(type=socket.SOCK_DGRAM)

# 给服务端发消息
client.sendto(b'hehe', ('127.0.0.1', 9000))
# 收消息
msg = client.recvfrom(1024)
print('收到服务端的回复：', msg)
client.close()
