# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 继承方法.py
# @Time : 2026/4/15 10:17

# 继承
class Student:
    name = None
    age = None
    __score =  None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"姓名：{self.name}")
        print(f"年龄：{self.age}")
        print(f"成绩：{self.__score}")

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

class Pupil(Student):
    def testing(self):
        print("小学生正在考试")

class CollegeStudent(Student):
    def testing(self):
        print("大学生正在考试")

student1 = Pupil("小王", 10)
student1.testing()
student1.set_score(90)
student1.show_info()
print("-" * 20)
student2 = CollegeStudent("小李", 22)
student2.testing()
student2.set_score(60)
student2.show_info()