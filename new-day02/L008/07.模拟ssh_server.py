#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import subprocess
import struct
import json

sock = socket.socket()      #服务端

sock.bind(("127.0.0.1",8900))


sock.listen(5)

while 1:
    print('server is working...')
    conn,addr = sock.accept()

    # conn.sendall("欢迎你！".encode("utf-8"))
    while 1:
        try:
            cmd = conn.recv(1024).decode("utf-8")
            print(cmd)
            if len(cmd) == 0 or cmd == "q":
                # print('aaa')
                break


            #在server端执行远程调用命令
            res = subprocess.Popen(
                cmd,
                shell=True,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
            )
            ret_stdout = res.stdout.read().decode("gbk")
            ret_stderr = res.stderr.read().decode("gbk")
            cmd_response_stdout_length = struct.pack("i",len(ret_stdout))
            cmd_response_stderr_length = struct.pack("i",len(ret_stderr))

            header_stdout_info = {
                "data_length": len(cmd_response_stdout_length),
                "filename":"a.txt",
                "md5_val":"1212fdsaf111244,"
            }
            header_stdout_info_json = json.dumps(header_stdout_info)
            header = len(header_stdout_info_json.encode("utf-8"))
            struct_header = struct.pack("i",header)
            if ret_stdout:
                print(struct.unpack("i",struct_header)[0])
                conn.sendall(struct_header)
                conn.sendall(header_stdout_info_json.encode("utf-8"))
                conn.sendall(ret_stdout.encode("utf-8"))
            else:
                conn.sendall(cmd_response_stderr_length)
                conn.sendall(ret_stderr.encode("utf-8"))
        except Exception as e:
            break
    conn.close()



