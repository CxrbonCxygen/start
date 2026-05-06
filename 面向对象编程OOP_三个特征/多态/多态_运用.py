# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 多态_运用.py
# @Time : 2026/4/22 10:58

class Animal:
    def cry(self):
        pass

class Dog(Animal):
    def cry(self):
        print("汪汪汪")

class Cat(Animal):
    def cry(self):
        print("喵喵喵")

class Pig(Animal):
    def cry(self):
        print("哼哼哼")

class Bird(Animal):
    def cry(self):
        print("叽叽喳喳")

# 在python中，子类对象可以传递给父类类型
def func(animal: Animal):
    animal.cry()
    print(f"animal类型是{type(animal)}")

cat = Cat()
dog = Dog()
pig = Pig()
bird = Bird()

func(cat)
func(dog)
func(pig)
func(bird)
print("-----------------------------------------------------------------------------------------------------------------")

# python中函数|方法的参数是没有类型限制的
# python比不要求严格的继承关系，关注的不是对象的类型本身，而是它是否具有调用的方法
class AA:
    def hi(self):
        print("hi")

class BB:
    def hi(self):
        print("hi")

def test(obj):
    obj.hi()

aa = AA()
bb = BB()
test(aa)
test(bb)