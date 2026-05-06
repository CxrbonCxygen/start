# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 子类与父类注意事项.py
# @Time : 2026/4/16 12:02

# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 调用父类成员.py
# @Time : 2026/4/16 11:49

# 子类不能直接访问父类私有成员

# 访问可以溯源父类

# 建议使用super()，不受命名影响

class A:
    n1 = 300
    n2 = 500
    n3 = 600

    def fly(self):
        print("A类中的fly方法")


class B(A):
    n1 = 200
    n2 = 400

    def fly(self):
        print("B类中的fly方法")


class C(B):
    n1 = 100

    def fly(self):
        print("C类中的fly方法")

    def say(self):
        print(self.n1) #100
        print(self.n2) #400
        print(self.n3) #600
        print(super().n1) #200
        print(B.n1) #200
        print(C.n1) #100

        self.fly()
        A.fly( self)
        super().fly()


c = C()
c.say()