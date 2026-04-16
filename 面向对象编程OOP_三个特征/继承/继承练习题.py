# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 继承练习题.py
# @Time : 2026/4/16 09:54

class GrandPa:
    name = "大头爷爷"
    age = 70
    hobby = "看电影"

class Father(GrandPa):
    name = "大头爸爸"
    age = 39

class Son(Father):
    name = "大头儿子"

son = Son()

print(f"son.name = {son.name} son.age ={son.age} son.hobby = {son.hobby}")

print("-"*20)

class Computer:
    CPU = None
    memory =  None
    disk = None

    def __init__(self, CPU, memory, disk):
        self.CPU = CPU
        self.memory = memory
        self.disk = disk
    def get_details(self):
        return f"CPU:{self.CPU} memory:{self.memory} disk:{self.disk}"


class PC(Computer):
    __brand = None  # 私有属性

    def __init__(self,CPU, memory, disk, brand):
        # 初始化子类属性
        super().__init__(CPU, memory, disk)
        self.__brand = brand

    def print_info(self):
        print(f"电脑品牌是:{self.__brand} {self.get_details()}")



class NotePad(Computer):
    __color =  None
    def __init__(self,CPU, memory, disk, color):
        super().__init__(CPU, memory, disk)
        self.__color = color
    def print_info(self):
        print(f"电脑颜色是:{self.__color} {self.get_details()}")


pc = PC("i5-9400", "16G", "1T", "华硕")
pc.print_info()