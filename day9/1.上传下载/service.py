#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket,subprocess
service = socket.socket()
service.bind(('127.0.0.1',8000))
service.listen(5)

while True:
    conn, addr = service.accept()
    while True:
        try:
            msg = conn.recv(1024)
            #1.接收到用户请求后发送结果长度
            obj = subprocess.Popen(
                msg.decode('utf8'),
                shell=True,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
            )

            stderr = obj.stderr.read()
            stdout = obj.stdout.read()

            ret = stdout if stdout else stderr

            total_bytes = len(ret)
            conn.send(str(total_bytes).encode('utf8'))
            #2.接收用户的认证信息
            is_ready = conn.recv(1024)
            if is_ready == b"RECV_OK":
                conn.send(ret)
            # print(msg.decode('utf8'))
        except Exception:
            break
    conn.close()
            # service.close()


service.close()


