
# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 成员方法内部调用.py
# @Time : 2026/4/9 09:44

class Dog:
    name = "波斯猫"
    age = None

    def info(self, name):
        print(f"name:{name}")
        print(f"name:{self.name}")

dog = Dog()
dog.info("小花")

# 可通过self.属性名 访问成员变量

