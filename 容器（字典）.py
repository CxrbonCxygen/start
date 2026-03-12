# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 容器（字典）.py
# @Time : 2026/3/12 09:05

# 元组、列表、集合都是单层容器
# 字典是多层容器
# 字典是无序的，可重复的
# 字典的键值对用冒号隔开，键和值用逗号隔开
# （）是元组，{}是字典，[]是列表，{}是集合
dict1 = {"name": "tom", "age": 18, "sex": "male", "name": "jack"}
# 字典的key通常是字符串，但是也可以是数字、元组、列表、对象等
# 字典的value可以是任意类型，但是key必须是不可变对象
# 字典不支持索引，但是可以通过key来访问value
# 不支持while遍历，但是可以通过for遍历
students = {
    "jom": {"name": "jom", "age": 18},
    "tom": {"name": "tom", "age": 19},
    "jack": {"name": "jack", "age": 20},
}
for key, name in students.items():
    print(key)
    print(name)
    print(name["name"])

# 创建空字典
dict2 = {}
dict3 = dict()
print(dict2,type(dict2))
print(dict3,type(dict3))
# 键值唯一，多的会覆盖

# 字典生成式
books = ["python", "java", "c++"]
authors = ["tom", "jack", "jom"]
dict4 = {book: author for book, author in zip(books, authors)}
print(dict4)
dict5 = {book:authors * 2 for book, authors in zip(books, authors)}
print(dict5)