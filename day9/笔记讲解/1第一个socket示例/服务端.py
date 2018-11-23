# -*- coding: utf-8 -*-

import socket

# 先要买电话
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket.AF_INET:基于网络的socket  socket.SOCK_STREAM：基于TCP的流式连接
# 插手机卡
phone.bind(('127.0.0.1', 8000))  # 端口：1~65535 ： 1~1024操作系统自用   剩下是应用程序可用的
# 开机
phone.listen(5)

# 等着客户端给我打电话
print('等啊等，等别人给我打电话！')
conn, addr = phone.accept()  # conn:代表连接  addr:对方的地址
print('来电话了！！')
print(conn, addr)
# 收消息
msg = conn.recv(1024)
print('对方的消息是：', msg)
# 回消息
# 字节类型  --->  字符串类型
msg_str = msg.decode('utf8')
# str(msg, encoding='utf8')
# 字符串   ----> 字节类型
answer = '{} sb'.format(msg_str).encode('utf8')
# bytes(msg_str.upper(), encoding='utf8')
conn.send(answer)
# 挂电话
conn.close()  # 关闭连接
# 关机
phone.close()  # 关闭服务

