# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 继承细节.py
# @Time : 2026/4/15 10:23

# 子类继承父类
# 子类不能用到父类的私有属性和方法
# 只能用父类的公共属性和方法，来调用父类的私有属性和方法

class Base:
    n1 = 10

    __n2 = 20

    def __init__(self):
        print("父类初始化方法")

    def hi(self):
        print("父类普通方法")

    def __hello(self):
        print("父类私有方法")

    # 提供公共方法访问父类的私有属和方法
    def test(self):
        print("test()获得父类非私有属性n1的值为：",self.n1)
        print("test()获得父类私有属性n2的值为：",self.__n2)
        self.hi()
        self.__hello()

class Sub(Base):
    # 子类构造器
    def __init__(self):
        print("子类初始化方法")

    def say_ok(self):
        # 父类非私有属性和方法可以访问
        print("say_ok()获得父类非私有属性n1的值为：",self.n1)
        self.hi()
        # 父类私有属性和方法不能访问
        # print("say_ok()获得父类私有属性n2的值为：",self.__n2)

sub = Sub()
print("-"*20)
sub.say_ok()
print("-"*20)
sub.test()

# int 查看类关系快捷键：Ctrl + H