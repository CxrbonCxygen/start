# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 重写.py
# @Time : 2026/4/21 13:46

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        return f"我的名字是{self.name}，今年{self.age}岁"


class Student(Person):
    def __init__(self, name, age, id, score):
        # 继承父类构造方法super()
        super().__init__(name, age)
        self.id = id
        self.score = score

    def say(self):
        return f"{super().say()}，我的ID是{self.id}，我的成绩是{self.score}"

person = Person("小王", 18)
print(person.say())

student = Student("小王", 18, 1001, 90)
print(student.say())