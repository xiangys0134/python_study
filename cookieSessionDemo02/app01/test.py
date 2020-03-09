#!/user/bin/env python3
# -*- coding: utf-8 -*-
import random
l1 = ["1","2"]

str_l1 = "".join(l1)
# print(str_l1)

list1 = [chr(i) for i in range(65,91)]
l2 = random.choice(list1)
print(l2)


list3 = [chr(i) for i in range(0,9)]

print(list3)