# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 练习题.py
# @Time : 2026/4/10 11:01

class A01:
    def max(self, lst):
        max = 0
        for i in lst:
            if i > max:
                max = i
        return max
    # 有一个默认的无参数构造函数

lst = [1.1,2.9,-1.9,46.9]
a = A01()
print("a 的最大值是：",a.max(lst))

print("-" * 20)

class Book :
    # 属性
    name = None
    price = None
    # 构造器
    def __init__(self,name,price):
        self.name = name
        self.price = price
    # 方法
    def update_price(self):
        if self.price > 150:
            self.price = 150
        elif self.price > 100:
            self.price = 100
    def info(self):
        print(f"这本书是：{self.name},价格是{self.price}")

javabook = Book("javabook",300)
javabook.info()
javabook.update_price()
javabook.info()

print("-" * 20)

class cirecle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

c = cirecle(5)
print(f"面积是：{c.area():.2f}")
print(f"周长是：{c.perimeter():.2f}")
print(f"周长是：{round(c.perimeter(),2)}")
print("-" * 20)

class cal:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        if self.b == 0:
            return print("除数不能为0")
        return self.a / self.b

c = cal(10,5)
print(f"他们相加为{c.add()}")
print(f"他们相减为{c.sub()}")
print(f"他们相乘为{c.mul()}")
print(f"他们相除为{c.div()}")
c = cal(10,0)
print(f"他们相除为{c.div()}")
print("-" * 20)

class Music:
    def __init__(self,name,singer):
        self.name = name
        self.singer = singer
    def info(self):
        print(f"歌名是：{self.name},歌手是：{self.singer}")
    def play(self):
        print(f"正在播放：{self.name}")

music = Music("I'm Yours","Lady Gaga")
music.info()
music.play()

print("-" * 20)

class Demo:
    i = 100

    def m(self):
        self.i += 1
        j = self.i
        print("i=",self.i)
        print("j=",j)

d1 = Demo()
d2 = d1
d2.m()
print("d1.i=",d1.i)
# d1.i = 101
print("d2.i=",d2.i)
# d2.i = 101

print("-" * 20)

import random

class RockPaperScissors:
    """剪刀石头布游戏"""
    def __init__(self):
        self.win = 0
        self.lose = 0
        self.draw = 0
    
    def play(self, player_choice):
        computer_choice = random.randint(0, 2)
        
        gestures = {0: "石头", 1: "剪刀", 2: "布"}
        print(f"你出了：{gestures[player_choice]}")
        print(f"电脑出了：{gestures[computer_choice]}")
        
        if player_choice == computer_choice:
            self.draw += 1
            print("平局！")
        elif (player_choice == 0 and computer_choice == 1) or \
             (player_choice == 1 and computer_choice == 2) or \
             (player_choice == 2 and computer_choice == 0):
            self.win += 1
            print("你赢了！")
        else:
            self.lose += 1
            print("你输了！")
    
    def show_score(self):
        print(f"\n战绩统计：")
        print(f"获胜次数：{self.win}")
        print(f"失败次数：{self.lose}")
        print(f"平局次数：{self.draw}")

game = RockPaperScissors()
print("=== 剪刀石头布游戏 ===")
print("0: 石头, 1: 剪刀, 2: 布")

while False:
    try:
        choice = int(input("\n请输入你的选择（0/1/2），输入-1退出："))
        if choice == -1:
            game.show_score()
            break
        if choice not in [0, 1, 2]:
            print("无效输入，请输入0、1或2")
            continue
        game.play(choice)
    except ValueError:
        print("请输入有效的数字！")
