#!/user/bin/env python3
# -*- coding: utf-8 -*-

import socket,subprocess,os,struct

sock = socket.socket()
sock.bind(("0.0.0.0",8800))
sock.listen(5)

while 1:
    conn,addr = sock.accept()
    conn.sendall("欢迎您".encode("utf-8"))

    while 1:
        try:
            cmd = conn.recv(1024)
            print("cmd",cmd.decode("gbk"))

            if cmd.decode("gbk") == "q":
                break

            res = subprocess.Popen(
                cmd.decode("gbk"),
                shell=True,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE
            )

            cmd_response = res.stdout.read()

            # print(cmd_response.decode("gbk"))
            print(len(cmd_response))

            header_info = {
                "data_length": len(cmd_response),
                "filename": "a.txt",
                "md5_val": "23132fdsfds"
            }

            import json
            header_info_json = json.dumps(header_info)

            header_info_length = struct.pack("i",len(header_info_json))
            conn.sendall(header_info_length)
            conn.sendall(header_info_json.encode("utf-8"))
            conn.sendall(cmd_response)
        except Exception as e:
            break
    conn.close()