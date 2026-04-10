# @Version : 1.0
# @Auther : CarbonOxygen
# @File : python支持对象动态的添加.py
# @Time : 2026/4/8 13:56

class Person:
    name = None
    age = None

    def ok(self):
        print("ok")

def hi():
    print("this module01 hello world")

p = Person()
p2 = Person()

# 动态添加成员方法
# m1是自己定义的方法名称，由程序员自行定义(只会给p，不会给p2)
# 会让m1方法和hi方法关联起来，调用m1，就会调用hi
# 注意：这里应该赋值函数对象 hi，而不是调用函数 hi()
p.m1 = hi
p.m1()

print(type(p.m1),type(hi),type(hi()))
print(type(p.ok()))
print(type(p.ok))