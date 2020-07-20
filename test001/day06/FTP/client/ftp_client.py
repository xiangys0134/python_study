#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket,os


sock = socket.socket()

sock.connect(('127.0.0.1',8800))

data = sock.recv(1024)
print("recv data:",data.decode('utf-8'))

while True:
    cmd = input('>>>')      #put xxxx.png
    # sock.sendall(cmd.encode('utf-8'))
    if cmd == 'q' or cmd == 'Q':
        break
    if len(cmd) == 0:
        print('0字节')
        break

    #解析cmd 示例：put xxxx.png
    action,filename = cmd.strip().split( )
    filesize = os.path.getsize(filename)

    #构建报头信息
    header_info = {
        "action": action,
        "filesize":filesize,
        "filename": filename,
    }

    import struct,json

    header_info_json = json.dumps(header_info).encode('utf-8')
    header_length = struct.pack("i",len(header_info_json))

    sock.sendall(header_length)

    sock.sendall(header_info_json)

    #上传文件
    with open(filename,'rb') as f:
        for line in f:
            sock.sendall(line)

sock.close()




