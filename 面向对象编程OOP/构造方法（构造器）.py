# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 构造方法（构造器）.py
# @Time : 2026/4/9 12:23

class Person:
    # python可以动态生成对象属性
    # name = None
    # age = None

    # 构造方法
    # 是完成对象的初始化操作
    def __init__(self, name, age):
        print(f"人物创建成功，名字：{name} 年龄：{age}")
        print(f"self的ID：{id( self)}")
        self.name = name
        self.age = age
    # 如果有多个构造方法，只有最后一个生效
    def __init__(self, name):
        print(f"人物创建成功，名字：{name}")
        # return "返回值"
    # 构造方法不能有返回值

# 创建对象
# p1 = Person("kobe", 18)
p1 = Person("kobe")
print(f"p1的ID：{id( p1)}")


