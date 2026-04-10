# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 对象作为参数传递.py
# @Time : 2026/4/9 12:12

class Person:
    name = None
    age = None

# 分析对象作为参数传递到函数
def f1(Person):
    print(f"（2）它的地址是{id(Person)}")
    Person.name = "小王"
    Person.age += 1

p1 = Person()

p1.name = "小张"
p1.age = 18

print(f"（1）它的地址是{id(p1)},它的名字：{p1.name},它的年龄：{p1.age}")
f1(p1)
print(f"（3）它的地址是{id(p1)},它的名字：{p1.name},它的年龄：{p1.age}")