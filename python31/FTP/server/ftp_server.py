#!/user/bin/env python3
# -*- coding: utf-8 -*-

import socket,subprocess,os,struct,json

sock = socket.socket()
sock.bind(("0.0.0.0",8800))
sock.listen(5)

while 1:
    conn,addr = sock.accept()
    conn.sendall("欢迎您".encode("utf-8"))

    while 1:
        try:
            header_length = struct.unpack("i",conn.recv(4))[0]
            header_info_json = conn.recv(header_length)

            header_info = json.loads(header_info_json.decode("utf-8"))

            print("header_info",header_info)

            action = header_info.get("action")
            filesize = header_info.get("filesize")
            filename = header_info.get("filename")

            with open(os.path.join('put_dir',filename),"wb") as f:
                has_reveived = 0
                while has_reveived < filesize:
                    data = conn.recv(1024)
                    f.write(data)
                    has_reveived += len(data)


        except Exception as e:
            print(e)
            break
    conn.close()