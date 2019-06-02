#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket,subprocess,struct,time

service = socket.socket()
service.bind(('127.0.0.1',8001))
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

            total_bytes = struct.pack('i',len(ret))
            print(total_bytes)
            conn.send(total_bytes)
            # print(msg.decode('utf8'),total_bytes,len(ret),'#',ret.decode('utf8'))
            conn.send(ret)
            # print(ret.decode('utf8'), '##################')


        except Exception:
            break
    conn.close()
            # service.close()


service.close()


