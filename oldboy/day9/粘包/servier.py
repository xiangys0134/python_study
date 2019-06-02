#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
1.开启一个ssocket连接
2.配置好监听
3.等待客户发起连接
4.接受命令
5.执行命令
6.返回结果

防止粘包：
1.首先传输玩命令之后将长度返回给客户端
2.客户端指定接收的字节长度
2.客户端发送相关的code
3.服务端接收过认证code后将数据结果传给客户

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
            total_size = len(ret)
            print(total_size,'################')
            conn.send(str(total_size).encode('utf8'))   #传输对应的参数
            read = conn.recv(1024)
            if read.decode() == "read_ok":
                print(ret.decode('gbk'))
                conn.send(ret)
        except Exception:
            break
            conn.close()
            server.close()

