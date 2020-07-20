#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket,subprocess,struct

sock = socket.socket()

sock.bind(('127.0.0.1',8800))

sock.listen(5)

while True:

    conn,addr = sock.accept()

    conn.sendall('欢迎您'.encode('utf-8'))
    while True:
        try:
            cmd = conn.recv(1024).decode('utf-8')
            print('rece data:',cmd)
            if len(cmd) == 0:
                print('0字节')
                break
            if cmd == 'q' or cmd == 'Q':
                break
            res = subprocess.Popen(
                cmd,
                shell=True,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
            )

            cmd_respones = res.stdout.read()
            # cmd_respones_length = struct.pack("i",len(cmd_respones))
            # print("len:",len(cmd_respones))
            header_info= {
                "data_length": len(cmd_respones),
                "filename": 'a.txt',
                "md5_VAL":'1213SDFSAF121313',
            }
            import json
            header_json_info = json.dumps(header_info)
            header_info_length = struct.pack("i",len(header_json_info))
            conn.sendall(header_info_length)
            conn.sendall(header_json_info.encode('utf-8'))
            conn.sendall(cmd_respones)
        except Exception as e:
            print(e)
            break

    conn.close()





