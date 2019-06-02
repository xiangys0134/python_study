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
while 1:
    try:
        cmd = conn.recv(1024)  # 获取要执行的系统命令  # ifconfig
        if len(cmd) <= 0:
            continue
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

        # 1. 先把执行结果的长度算出来，给客户端发过去
        total_size = len(ret)
        conn.send(str(total_size).encode('utf8'))
        # 2. 等待客户端给我传准备好了的信号
        is_ready = conn.recv(1024)
        if is_ready == b'RECV READY':
            # 3. 把执行结果发送给客户端
            # 返回执行结果
            conn.send(ret)
    except ConnectionResetError:
        conn.close()
        break
server.close()



