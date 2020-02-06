#!/user/bin/env python3
# -*- coding: utf-8 -*-
from django.db import models

class Publish():
    name="aaaa"
    title='你好'

    def sleep(self):
        pass

    list = []

    def __str__(self):
        return self.name


pub = Publish

# print(Publish.title)
#
# print(getattr(pub,"__str__"))

l1 = []
l2 = ['a','b','c']

l1.extend(l2)

print(l1)

# print(Publish.sleep)