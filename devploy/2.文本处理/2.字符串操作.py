#!/usr/bin/python
# -*- coding: utf-8 -*-

fruits = ['orange','apple','banana','pear']

starement = fruits[0]

for item in fruits[1:]:
    starement = starement + ',' +item

print(starement)

print(','.join(fruits))