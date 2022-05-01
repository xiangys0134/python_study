#!/user/bin/env python3
# -*- coding: utf-8 -*-

lst1 = [1,1,2,3,5,6]

s1 = set(lst1)

lst2 = [1,5,6,7,8,9]

s2 = set(lst2)

# print(s1,s2)

print(s1 & s2)
print(s1 | s2)
print(s1 - s2)


