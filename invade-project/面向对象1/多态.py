#!/user/bin/env python3
# -*- coding: utf-8 -*-


class AliPay:
    def pay(self,money):
        pass

class WechtPay:
    pass

class Person:
    pass

alex = Person()

ali_obj = AliPay()

def pay(name,payobj,money):
    payobj.pay(name,money)


pay(alex,ali_obj,100)
