# @Version : 1.0
# @Auther : CarbonOxygen
# @File : cat.py
# @Time : 2026/4/8 13:02
from asyncio.windows_events import NULL


# 定义cat 类
class Cat:
    age = None
    name = None
    color =  None

# 创建对象
cat1 = Cat()

# 赋值
cat1.age = 2
cat1.name = "Tom"
cat1.color = "white"

# 通过对象.属性，访问属性
print(f"it is name {cat1.name}")

# 类是抽象的，对象是具体的。
# 类是对象的模板，对象是类的实例。
# 栈内存中存放的是对象引用，对象引用会指向对象在堆中的地址

# 属性也被称为：成员变量
# 方法也被称为：成员函数

cat2 = Cat()
print(f"it is {cat2.name}")
cat2.color = "white"

# 两个对象ID不同
print(id(cat1))
print(id(cat2))
# 两个对象属性值相同，则属性ID相同
print(id(cat1.color))
print(id(cat2.color))