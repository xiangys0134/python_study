#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sock = socket.socket()      #服务端

sock.bind(("127.0.0.1",8900))


sock.listen(5)

while 1:
    print('server is working...')
    conn,addr = sock.accept()

    conn.sendall("欢迎你！".encode("utf-8"))
    while 1:
        try:
            data = conn.recv(1024).decode("utf-8")
            print(data)
            if len(data) == 0 or data == "q":
                print('aaa')
                break
            data = input("回复>>>>").encode("utf-8")
            conn.sendall(data)
        except Exception as e:
            break
    conn.close()



