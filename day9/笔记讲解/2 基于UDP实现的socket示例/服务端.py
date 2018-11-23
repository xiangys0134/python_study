# -*- coding: utf-8 -*-
"""
UDP 服务端
"""


import socket

# 创建服务
server = socket.socket(type=socket.SOCK_DGRAM)
# 绑定端口
server.bind(('127.0.0.1', 9000))
print('服务端已启动， 等待别人来给我发消息！')
# 收消息
msg, addr = server.recvfrom(1024)
print(msg)
print(addr)

# 发消息
server.sendto(b'udp OK', addr)
server.close()