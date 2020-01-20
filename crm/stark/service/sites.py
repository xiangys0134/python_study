#!/usr/bin/env python
# -*- coding:utf-8 -*-

class ModelStark():
    def __init__(self,model):
        self.model = model


class StarkSite():
    def __init__(self):
        self.__registry = {}
        self.__list2 = [1,2,3]

    def register(self,model,admin_class=None):
        admin_class = admin_class or ModelStark
        self.__registry[model] = admin_class(model)


site = StarkSite()

print(site.__list2)
