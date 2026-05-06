# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 多态_优化.py
# @Time : 2026/4/22 12:39

class Food:

    def __init__(self, name):
        self.name = name

class Fish(Food):
    pass

class Bone(Food):
    pass

class Grass(Food):
    pass

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Horse(Animal):
    pass

class Master:
    def __init__(self, name):
        self.name = name

    # def give_cat_food(self, cat: Cat, food: Food):
    #     print(self.name,"给", cat.name, "一个", food.name)
    #
    # def give_dog_food(self, dog: Dog, food: Food):
    #     print(self.name,"给", dog.name, "一个", food.name)

    # 使用多态
    def give_food(self, animal: Animal, food: Food):
        print(self.name,"给", animal.name, "一个", food.name)

master = Master("小米")
cat = Cat("小花")
fish = Fish("小红鱼")
dog = Dog("小汪")
bone = Bone("小骨")
horse = Horse("小马")
grass = Grass("小草")


# master.give_cat_food(cat, fish)
# master.give_dog_food(dog, bone)
master.give_food(cat, fish)
master.give_food(dog, bone)
master.give_food(horse, grass)