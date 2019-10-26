# -*- coding: utf-8 -*-


class A(object):
    country = 'China'
    __secret = '嘿嘿'

    # 创建实例
    def __new__(cls, *args, **kwargs):
        # cls: 表示类本身
        print('要创建对象啦')
        # 我们重写__new__方法时, 一定是创建好一个对象再对对象做定制化操作
        new_obj = super().__new__(A)
        new_obj.hobby = '吹牛逼'
        return new_obj

    # 初始化方法
    def __init__(self, name):
        print('要初始化对象啦')
        # self:表示实例本身
        self.name = name

    # 实例方法
    def dream(self):
        print('我是锦鲤双11买啥都不要钱!')

    # 属性方法:计算年龄,圆的面积和周长
    @property
    def age(self):
        # 经过一系列复杂的运算得到一个年龄
        return 100

    # 类方法:
    @classmethod
    def eat(cls):
        print('吃吃吃')

    # 静态方法
    @staticmethod
    def zuoditie():
        print('坐地铁真好玩!')

    def __yue(self):
        print('约吗?')

    def __str__(self):
        return '我是一个A类的对象'


# 类的实例化
obj = A('Alex')
# 访问对象属性
print(obj.name)
# # 先在对象上找,找不到就往类里面找
print(obj.country)
print(obj.hobby)

# 实例调用方法
obj.dream()
# 调用属性方法
print(obj.age)

# 调用类方法
A.eat()

# 调用静态方法
obj.zuoditie()

print(obj)
