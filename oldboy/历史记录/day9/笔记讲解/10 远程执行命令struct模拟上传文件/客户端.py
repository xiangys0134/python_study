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
import json

client = socket.socket()
client.connect(('127.0.0.1', 8090))


data = {
    "file_name": "xx.avi",
    "file_size": 1024*1024*1024,
    "MD5": "wqe121313131wqs"
}

# 使用json序列化数据
header = json.dumps(data)
header_bytes = header.encode('utf8')
header_size = len(header_bytes)
header_data = struct.pack('i', header_size)
client.send(header_data)
# 把header_bytes发送给服务端
client.send(header_bytes)
# 上传文件
# with open('xx.avi', 'rb') as f:
#     client.send(f.read(1024))

# ...
# 关闭链接
client.close()
