#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess,socket





service = socket.socket()
service.bind(('127.0.0.1',8004))
service.listen(3)

conn,addr = service.accept()

while True:
    try:
        msg = conn.recv(1024)

        obj = subprocess.Popen(
            msg.decode('utf8'),
            shell=True,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE
        )

        ret = obj.stdout.read() if obj.stdout else obj.stderr.read()

        conn.send(ret)
    except Exception:
        raise EOFError

conn.close()

service.close()