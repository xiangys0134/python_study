#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import struct
import json
import hashlib
import os

sk = socket.socket()
sk.bind(('127.0.0.1',8000))
sk.listen(5)

class My_socket:
    def __init__(self,conn):
        self.conn,self.addr = conn.accept()

    def myrecv(self,buffer=1024):
        msg = self.conn.recv(buffer)
        return msg
        # while recv_leng < buffer:
        #     recv_data = self.conn.recv(1024)

            # if buffer <= 1024:
            #     msg = self.conn.recv(buffer)
            #     recv_data += msg
            #     return recv_data
            #     break
            # else:
            #     # while recv_leng <= buffer:
            #     recv_data += self.conn.recv(1024)
            #     recv_leng += len(recv_data)
            #     buffer -= 1024
                # buffer -= 1024
            # return myrecv * myrecv(self,buffer=buffer,recv_leng=recv_leng,recv_data=recv_data)
        # msg = self.conn.recv(buffer)
        # return msg
            # return
        # return msg

    def mysend(self,msg):
        self.conn.send(msg)




    #服务端第一次获取到字典
if __name__ == '__main__':
    while True:
        server = My_socket(sk)
        msg = server.myrecv(4)
        dic_byte = struct.unpack('i',msg)[0]
        print(dic_byte)
        msg = server.myrecv(dic_byte)   #收到字典

        # server.mysend(b'read_ok')
        # with open()
        print(msg)
        msg = msg.decode('utf8')
        msg = json.loads(msg)


        # ftp_msg = server.myrecv(msg['file_size'])

        print(msg['file_size'],'##################')

        recv_leng = 0
        m = hashlib.md5()
        # if os.path.exists(msg['file_name']):os.
        with open(msg['file_name'],'wb') as f:
            while recv_leng < msg['file_size']:
                f.seek(recv_leng)
                recv_data = server.myrecv(1024)
                f.write(recv_data)
                recv_leng += len(recv_data)
                # f.write(ftp_msg)
                m.update(recv_data)
            md5_id = m.hexdigest()

        #获取字典
        msg = server.myrecv(4)
        dic_byte = struct.unpack('i', msg)[0]
        print(dic_byte)
        msg = server.myrecv(dic_byte)  # 收到字典
        msg = msg.decode('utf8')

        # msg = json.loads(msg)
        # print(msg)
        # print(md5_id)
        #
        # if str(md5_id) == str(msg['md5']):
        #     print('md5值正确',md5_id)






