# -*- coding: utf-8 -*-


s = 'Hello world!'
# 字符串 --> 字节
print(s.encode('utf8'))
print(bytes(s, encoding='utf8'))


b = b'Hello world!'
# 字节  --> 字符串
print(b.decode('utf8'))
print(str(b, encoding='utf8'))
