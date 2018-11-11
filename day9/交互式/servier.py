#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
1.开启一个ssocket连接
2.配置好监听
3.等待客户发起连接
4.接受命令
5.执行命令
6.返回结果
"""

import socket,subprocess

server = socket.socket()
server.bind(('127.0.0.1',8090))
server.listen(5)
print('开始等待连接')
while True:
    conn,addr = server.accept()

    while True:
        try:
            cmd = conn.recv(1024)
            print(cmd.decode('utf8'))
            obj = subprocess.Popen(
                cmd.decode('utf8'),
                shell=True,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE
            )

            err_data = obj.stderr.read()
            out_data = obj.stdout.read()

            ret = err_data if err_data else out_data
            print(ret.decode('gbk'))
            conn.send(ret)
        except Exception:
            break
            conn.close()
            server.close()

