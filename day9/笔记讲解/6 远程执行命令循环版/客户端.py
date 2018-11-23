# -*- coding: utf-8 -*-
"""
1. 创建socket client
2. 链接服务端
3. 等待用户输入系统命令
4. 把命令发送给服务端
5. 等着收结果
"""

import socket

client = socket.socket()
client.connect(('127.0.0.1', 8090))

while 1:
    cmd = input('>>>:').strip()
    # 输入exit退出：
    if cmd.upper() == 'EXIT':
        break
    client.send(cmd.encode('utf8'))
    # 等着收结果
    ret = client.recv(1024)
    print('执行结果：')
    print(ret.decode('gbk'))
# 关闭链接
client.close()
