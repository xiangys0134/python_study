# -*- coding: utf-8 -*-
"""
1. 起一个socket server服务
2. 等着客户端发来系统命令
3. 执行系统命令
4. 给客户端返回结果
"""

import socket
import subprocess

server = socket.socket()
server.bind(('127.0.0.1', 8090))
server.listen(5)
# 等待连接
conn, addr = server.accept()
cmd = conn.recv(1024)  # 获取要执行的系统命令
# 使用subprocess模块
obj = subprocess.Popen(
    cmd.decode('utf8'),  # 把收到的字节数据转换成字符串
    shell=True,
    stderr=subprocess.PIPE,
    stdout=subprocess.PIPE
)
err_data = obj.stderr.read()
out_data = obj.stdout.read()

ret = err_data if err_data else out_data
# 返回执行结果
conn.send(ret)

conn.close()
server.close()



