#!/usr/bin/env python
# -*- coding:utf-8 -*-

class A:
    pass

class B(A):
    pass

# print(issubclass(B,A))

a = A()
b = B()

print(isinstance(a,A))
print(isinstance(b,A))
print(isinstance(a,B))