#!/usr/bin/env python
# -*- coding:utf-8 -*-


def outer():
    a = 1
    b = 'str'
    def inner():
        print(a,b)
    return inner



def read():
    with open("file",'r',encoding="utf8") as f1:
        content = f1.read()

    def inner():
        return content
    return inner

inn =read()

content = inn()
print(content)