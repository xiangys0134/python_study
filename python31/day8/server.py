#!/user/bin/env python3
# -*- coding: utf-8 -*-

import socketserver,struct

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            try:
                data = self.request.recv(1024)  # 阻塞
                print(data.decode("utf-8"))
                if not len(data) or data.decode("utf-8") == "q":
                    print("=====")
                    break
                res = input("回复>>>").encode("utf-8")
                self.request.sendall(res)
            except Exception as e:
                print(e)
                break

server = socketserver.ThreadingTCPServer(("127.0.0.1",8800),MyServer)

server.serve_forever()