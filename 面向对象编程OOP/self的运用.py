# @Version : 1.0
# @Auther : CarbonOxygen
# @File : self的运用.py
# @Time : 2026/4/9 10:07

# 成员方法转静态方法
class Dog:
    name = "小白"
    age = 1

    # 隐式传入
    def hi(self):
        print(f"hi self:{id(self)}")

    def eat(self):
        print("吃吃吃")
    def my_name(self):
        print(f"我的name是{self.name}")
    def cry(self):
        print(f"{self.name} is crying")
    # 转为静态方法，可以不带self参数
    # 调用静态方法，不需要创建对象
    @staticmethod
    def run():
        print("跑跑跑")

# 方法一：通过对象调用
d = Dog()
d.run()
d.eat()
# 方法二：通过类名调用
Dog.run()



# self表示当前对象本身
# 那个对象调用这个方法，self就表示那个对象
dog2 = Dog()
print(f"dog2:{id(dog2)}")
dog2.hi()
d.hi()

dog2.my_name()
dog2.cry()
print("-" * 20)
dog2.name = "小黑"
dog2.my_name()
dog2.cry()
print("-" * 20)


# 课堂练习
class Person:
    name = "小王"
    age = 18

    def compare_to(self, other):
        if self.name == other.name and self.age == other.age:
            return "他们是同一个人"
        elif self.age < other.age:
            return f"{self.name}比{other.name}小"
        elif self.age > other.age:
            return f"{self.name}比{other.name}大"
        else:
            return f"{self.name}和{other.name}一样大"


p1 = Person()
p2 = Person()
print(p1.compare_to(p2))
p1.name = "小li"
print(p1.compare_to(p2))
p1.age = 20
print(p1.compare_to(p2))