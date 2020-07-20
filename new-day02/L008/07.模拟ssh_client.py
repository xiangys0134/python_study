#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import struct
import json

sock = socket.socket()

sock.connect(("127.0.0.1",8900))


while 1:
    # res = sock.recv(1024)
    # print(res.decode("utf-8"))

    data = input("shell>>>>")
    sock.sendall(data.encode("utf-8"))
    if data=="q":
        break
    #接收报头
    header = sock.recv(4)
    response_length = struct.unpack("i",header)[0]
    print(response_length)



    header_data = sock.recv(response_length)
    ret = json.loads(header_data.decode("utf-8"))
    response_data_length = ret["data_length"]
    print(response_data_length)
    print(ret["filename"])

    recv_data = b""
    has_recevied = 0
    while response_data_length > has_recevied:
        recv = sock.recv(1024)
        recv_data += recv
        has_recevied += len(recv)

    print(recv_data.decode("utf-8"))
sock.close()



