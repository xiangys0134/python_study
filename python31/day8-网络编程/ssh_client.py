#!/user/bin/env python3
# -*- coding: utf-8 -*-
import socket,struct

sock = socket.socket()

sock.connect(("127.0.0.1",8800))

data = sock.recv(1024)
print("rece data:",data.decode("utf-8"))

while 1:
    cmd = input(">>>")
    sock.sendall(cmd.encode("gbk"))

    if cmd == "":
        continue

    if cmd == "q":
        break

    #接收消息
    data = sock.recv(4)
    data_length = struct.unpack("i",data)
    data_length = data_length[0]

    import json
    header_info = sock.recv(data_length)
    header_info_json = json.loads(header_info)


    print("data_length:",data_length)
    # data_recv = 0
    recv_data = b""
    has_reveived = 0
    while has_reveived < header_info_json["data_length"] :
        data = sock.recv(1024)
        recv_data += data
        has_reveived += len(data)

    print("response:",recv_data.decode("gbk"))

sock.close()
