#!/user/bin/env python3
# -*- coding: utf-8 -*-
from queue import Queue
q = Queue()
for i in range(1, 255):
    host_ip = "192.168.0.%s" % i
    q.put(host_ip)

print(q,type(q))
print(q.get_nowait())
print(q.get_nowait())