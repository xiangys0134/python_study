#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket,subprocess,struct,json,os

sock = socket.socket()

sock.bind(('127.0.0.1',8800))

sock.listen(5)

while True:

    conn,addr = sock.accept()

    conn.sendall('欢迎您'.encode('utf-8'))
    while True:
        try:
            pack_length = conn.recv(4)
            header_length = struct.unpack("i",pack_length)[0]

            header_info_json = conn.recv(header_length)

            header_info = json.loads(header_info_json.decode('utf-8'))
            print(header_info)

            action = header_info.get("action")
            filesize = header_info.get("filesize")
            filename = header_info.get("filename")

            # response_length = len(filesize)


            with open(os.path.join("putdir",filename),'wb') as f:
                # recv_data = b''
                has_reveived = 0
                while has_reveived < filesize:
                    data = conn.recv(1024)
                    f.write(data)
                    has_reveived += len(data)
        except Exception as e:
            print(e)
            break

    conn.close()





