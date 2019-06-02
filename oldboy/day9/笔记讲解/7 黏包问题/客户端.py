# -*- coding: utf-8 -*-
"""
基于TCP的socket会出现黏包问题
客户端
"""

import socket
import time

client = socket.socket()

client.connect(('127.0.0.1', 8091))

client.send(b'H')
# time.sleep(1)
client.send(b'ello')
# time.sleep(1)
client.send(b'world')

client.close()