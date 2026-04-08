# @Version : 1.0
# @Auther : CarbonOxygen
# @File : person.py
# @Time : 2026/4/8 13:14

class Person:
    age = None
    name = None

# 两个对象指向同一个对象地址，会改变对象值
p1 = Person()
p1.age = 18
p1.name = "Tom"
p2 = p1
print(id(p1))
print(p2.name)
p2.name = "Jack"
print(p1.name)

p2 = None
print(p1.name)
# print(p2.name)