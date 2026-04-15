# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 成员方法.py
# @Time : 2026/4/8 13:33

# def 方法名(self,参数):
#     方法体
#     return 返回值

# 在方法定义的参数列表中有一个参数self，这个参数是必须的
# self表示当前对象本身
# 通过对象调用方法时，self会隐式传入
# 方法内部，需要用到self，才能访问到成员变量

class Person:
    # 成员变量
    name =  None
    age = None

    # 成员方法
    def hi(self):
        print("hi python")

    def cal01(self):
        sum = 0
        for i in range(1,1001):
            sum += i
        return sum

    def cal02(self, n):
        sum = 0
        for i in range(1,n+1):
            sum += i
        return sum

    def get_sum(self, a, b):
        return a + b

p = Person()
p.hi()
print(p.cal01())
print(p.cal02(1000))
print(p.get_sum(1,2))
print(p.get_sum(p.cal01(),p.cal02(1000)))

