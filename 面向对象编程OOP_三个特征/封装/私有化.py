# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 私有化.py
# @Time : 2026/4/10 12:20

class Clerk:
    name = None
    age = None
    # 私有属性
    __job = None
    __salary = None
    # 私有属性也可以动态生成
    def __init__(self, name, job, salary):
        self.name = name
        self.__job = job
        self.__salary = salary
    def set_job(self, job):
        self.__job = job
    def get_job(self):
        return self.__job
    # 私有方法
    def __get_salary(self):
        return self.__salary
    def get_salary(self):
        return self.__get_salary()

clerk = Clerk("kobe", "程序员", 10000)
print(clerk.name)
# 私有属性不能直接访问
# print(clerk.__job)
# 可以提供公共方法访问
print(clerk.get_job())
clerk.set_job("经理")
print(clerk.get_job())
# 私有方法不能直接访问
# print(clerk.__get_salary())
# 可以提供公共方法访问
print(clerk.get_salary())