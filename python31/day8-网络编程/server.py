#!/user/bin/env python3
# -*- coding: utf-8 -*-

import socket,socketserver

sock = socket.socket()

sock.bind(("0.0.0.0",8800))

sock.listen(5)

conn,addr = sock.accept()

data = conn.recv(1024)

print(data)

