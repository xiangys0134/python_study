#!/usr/bin/python
# -*- coding: utf-8 -*-
import copy

# lst = [1,2,3,4]
#
# new_lst = copy.copy(lst)
#
# print(new_lst,lst)
# print(id(new_lst),id(lst))
#
# new_lst.append({'key','value'})
# print(new_lst,lst)

dic = {'key':'v'}
lst = [1,2,3,4,dic]

new_lst = copy.deepcopy(lst)

print(new_lst,lst)

dic['key'] = 'value'
print(new_lst,lst)

