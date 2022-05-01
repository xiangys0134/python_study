#!/user/bin/env python3
# -*- coding: utf-8 -*-
import socket
sock = socket.socket()

sock.connect(("127.0.0.1",8800))

# data = sock.recv(1024)
# print(data.decode("utf8"))
# sock.sendall(b'aaa')

flag = 1
while flag:
    data = input(">>>")
    sock.sendall(data.encode("utf-8"))

    if data == "q":
        break

    response_data = sock.recv(1024)
    print("response:",response_data.decode("utf-8"))

