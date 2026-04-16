# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 多重继承.py
# @Time : 2026/4/15 12:04
from symtable import Class

class A:
    n1 = 10
    def m1(self):
        print("A类中的m1方法")

class B:
    n1 = 20
    def m2(self):
        print("B类中的m2方法")
    def m3(self):
        print(f"B类中m3方法，n1的值为{self.n1}")

class D:
    n1 = 30
    def m3(self):
        print("D类中的m3方法")

class C(A,B,D):
    n1 = 40
    pass # 占位，避免报错，不做任何操作

c = C()
print("")
c.m1()
print( "")
c.m2()
print("")
# 出现同名，左边类优先级高
print(c.n1)
c.m3()