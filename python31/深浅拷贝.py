#!/user/bin/env python3
# -*- coding: utf-8 -*-

import copy

lst = [1,2,3]

new_lst = copy.copy(lst)

print(new_lst)
print(id(lst),id(new_lst))