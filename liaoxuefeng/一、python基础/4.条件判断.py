#!/usr/bin/env python
# -*- coding:utf-8 -*-

age = 2
if age >= 18:
    print('your age is',age)
else:
    print('未成年')


s = input('birth:')
birth = int(s)

if birth < 2000:
    print('00前')
else:
    print('00后')
