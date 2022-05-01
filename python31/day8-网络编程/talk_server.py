#!/user/bin/env python3
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()

IP_PORT = ("0.0.0.0",8800)

sock.bind(IP_PORT)
sock.listen(5)

while 1:
    conn,addr = sock.accept()

    print("conn:",conn,"addr:",addr)
    conn.sendall('欢迎您'.encode("utf-8"))
    flag = 1

    while flag:
        try:
            data = conn.recv(1024)  #阻塞
            print(data.decode("utf-8"))
            if not len(data) or data.decode("utf-8") == "q":
                print("=====")
                break
            res = input("回复>>>").encode("utf-8")
            conn.sendall(res)
        except Exception as e:
            print(e)
            break

conn.close()

