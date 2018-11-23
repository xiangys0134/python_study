# -*- coding: utf-8 -*-
"""
1. 起一个socket server服务
2. 等着客户端发来系统命令
3. 执行系统命令
4. 给客户端返回结果
"""

import socket
import subprocess
import struct
import json

server = socket.socket()
server.bind(('127.0.0.1', 8090))
server.listen(5)
# 等待连接
conn, addr = server.accept()

header_data = conn.recv(4)  # 获取header信息
# 解包
header_size = struct.unpack('i', header_data)[0]
# 接受制定长度的header数据
header_bytes = conn.recv(header_size)

# 使用json模块把数据反序列化出来
data = json.loads(header_bytes)
print('接收到的头部数据是：', data)
# 拿到要上传的文件的名字、文件大小和MD5值
filesize = data.get('file_size')
filename = data.get('file_name')
md5 = data.get('md5')

# 要接收的文件大小比较大
# recv_size = 0
#
# with open(filename, 'wb') as f:
#     while recv_size < filesize:
#         recv_data = conn.recv(1024)
#         f.write(recv_data)
#         recv_size += len(recv_data)
#

conn.close()

server.close()



