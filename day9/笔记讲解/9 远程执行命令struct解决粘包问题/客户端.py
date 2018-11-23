# -*- coding: utf-8 -*-
"""
1. 创建socket client
2. 链接服务端
3. 等待用户输入系统命令
4. 把命令发送给服务端
5. 等着收结果
"""

import socket
import struct

client = socket.socket()
client.connect(('127.0.0.1', 8090))

while 1:
    cmd = input('>>>:').strip()
    print('输入的内容是：', cmd)
    # 输入exit退出：
    if cmd.upper() == 'EXIT':
        break
    if not cmd:
        continue
    client.send(cmd.encode('utf8'))
    # 1. 先获取执行结果的长度，做好接收的准备
    total_size_bytes = client.recv(4)
    # 用struct解包
    total_size = struct.unpack('i', total_size_bytes)[0]
    print('我要接受的数据量是：', total_size)
    # 等着收结果
    ret = client.recv(total_size)
    print('执行结果：')
    print(ret.decode('gbk'))
# 关闭链接
client.close()
