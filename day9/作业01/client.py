#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import struct
import os
import json
import hashlib

dic = {}


class Myclient:
    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(('127.0.0.1',8000))

        pass

    def myrecv(self,buffer=1024):
        msg = self.sk.recv(buffer)
        return msg

    def mysend(self,msg):
        self.sk.send(msg)

if __name__ == '__main__':
    while True:
        info = input(r'请输入要上传路径：').strip()
        if os.path.exists(info):
            # print(info)
            get_size = os.path.getsize(info)
            base_name = os.path.basename(info)
            dic['file_size'] = get_size
            dic['file_name'] = base_name

            #传文件名称过去
            file_msg = json.dumps(dic)
            print(file_msg,type(file_msg))
            byte_msg = struct.pack('i',len(file_msg.encode('utf8')))
            client = Myclient()
            client.mysend(byte_msg)

            client.mysend(file_msg.encode('utf8'))

            with open(info,'rb') as f:
                md5 = hashlib.md5()
                f_leng = 0
                data = b''
                send_size = 0
                print(dic['file_size'],'##################')
                for line in f:
                    client.mysend(line)
                    send_size += len(line)
                    md5.update(line)




                # while True:
                #     if f_leng < dic['file_size']:
                #         f_byte = f.read(1024)
                #         client.mysend(f_byte)
                #         # data += msg
                #         md5.update(f_byte)
                #         f_leng += len(f_byte)

                # print('aaaa')
                # sek_id = 0
                # # while True:
                # f_msg = f.read(dic['file_size'])
                # client.mysend(f_msg)
                    # if not f_msg:
                    #     break
                    # client.mysend(f_msg)
                    # sek_id += 1024
                    # f.seek(sek_id)

                # md5 = hashlib.md5()
                # md5.update(f_msg)
                dic['md5'] = md5.hexdigest()
                print(dic,send_size)

                #再将包拿出来
                file_msg = json.dumps(dic)
                print(file_msg, type(file_msg))
                byte_msg = struct.pack('i', len(file_msg.encode('utf8')))
                client.mysend(byte_msg)
                print(len(file_msg.encode('utf8')),byte_msg,file_msg,type(file_msg))
                client.mysend(file_msg.encode('utf8'))
                # client.mysend()








        # print(get_size)
