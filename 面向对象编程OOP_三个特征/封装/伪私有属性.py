# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 伪私有属性.py
# @Time : 2026/4/13 12:12

class Clerk:
    name = None

    __job = None
    __salary = None

    def __init__(self, name, job, salary):
        self.name = name
        self.__job = job
        self.__salary = salary

    def get_job(self):
        return self.__job

    def get_salary(self):
        return self.__salary
# 使用类定义的job，与私有job不一样
# 因为会动态生成新的私有属性:__job
# 内部原有的私有属性前面有类名如：_Clerk__job（可以打断点调试）
clerk = Clerk('小王', '程序员', 5000)
clerk.__job = '老师'
print(f"job:{clerk.__job}")
print(f"job:{clerk.get_job()}")
print("ok")
print(f"{id(clerk.__job)}")
print(f"{id(clerk.get_job())}")