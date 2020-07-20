#!/usr/bin/env python
# -*- coding:utf-8 -*-


#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket

sock = socket.socket()

sock.connect(("127.0.0.1",8900))


while 1:
    res = sock.recv(1024)
    print(res.decode("utf-8"))

    data = input("回复>>>>")
    sock.sendall(data.encode("utf-8"))
    if data=="q":
        break

sock.close()



