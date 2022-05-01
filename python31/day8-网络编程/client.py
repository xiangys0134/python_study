#!/user/bin/env python3
# -*- coding: utf-8 -*-
import socket

sock = socket.socket()

sock.connect(("127.0.0.1",8800))

sock.send(b"aaaa")