# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 调用父类成员.py
# @Time : 2026/4/16 11:49

# 子类和父类出现同名成员，子类优先级高
# 可以通过父类名、super（）访问父类成员

# 访问成员变量
# 父类名.成员变量名
# super().成员变量名
# 访问成员方法
# 父类名.成员方法名()
# super().成员方法名()

class A:
    n1 = 100

    def run(self):
        print("A类中的run方法")


class B(A):
    n1 = 200

    def run(self):
        print("B类中的run方法")

    # say 方法
    def say(self):
        print(f"父类中的n1:{A.n1}\n"
              f"本类中的n1:{self.n1}") # 如果本类没有本类成员变量，则访问父类成员变量
        A.run(self) # 通过父类名访问父类成员方法
        self.run()

    def hi(self):
        print(f"父类中的n1:{super().n1}")
        super().run()

b = B()
b.say()
print("-"*20)
b.hi()