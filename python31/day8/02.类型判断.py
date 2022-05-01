#!/user/bin/env python3
# -*- coding: utf-8 -*-

class A:
    pass

class B(A):
    pass

class C(B):
    pass

a = A()
print(isinstance(a,A))