#!/user/bin/env python3
# -*- coding: utf-8 -*-
import socket,struct,os,json

sock = socket.socket()

sock.connect(("127.0.0.1",8800))

data = sock.recv(1024)
print("rece data:",data.decode("utf-8"))

while 1:
    cmd = input(">>>")  #put 1.png

    if cmd == "":
        continue

    if cmd == "q":
        break

    action,filename = cmd.split(" ")

    filesize = os.path.getsize(filename)

    header_info = {
        "action": action,
        "filesize": filesize,
        "filename": filename
    }

    header_info_json = json.dumps(header_info).encode("utf-8")
    header_length = struct.pack("i",len(header_info_json))

    #发送报头信息长度
    sock.sendall(header_length)

    sock.sendall(header_info_json)

    with open(filename,'rb') as f:
        for line in f:
            sock.sendall(line)

sock.close()
