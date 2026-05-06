# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 多态_引入.py
# @Time : 2026/4/22 10:36

class Food:

    def __init__(self, name):
        self.name = name

class Fish(Food):
    pass

class Bone(Food):
    pass

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Master:
    def __init__(self, name):
        self.name = name

    def give_cat_food(self, cat: Cat, food: Food):
        print(self.name,"给", cat.name, "一个", food.name)

    def give_dog_food(self, dog: Dog, food: Food):
        print(self.name,"给", dog.name, "一个", food.name)


master = Master("小米")
cat = Cat("小花")
fish = Fish("小红鱼")
dog = Dog("小汪")
bone = Bone("小骨")

master.give_cat_food(cat, fish)
master.give_dog_food(dog, bone)

