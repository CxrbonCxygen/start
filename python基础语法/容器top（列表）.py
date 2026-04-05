# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 容器.py
# @Time : 2026/3/5 10:27
from unittest.util import three_way_cmp

hen1 = 3
hen2 = 5
hen3 = 1
hen4 = 3.4
hen5 = 2
hen6 = 50
avg_weight = (hen1 + hen2 + hen3 + hen4 + hen5 + hen6) / 6
print(f"hens' average weight is {avg_weight:.2f}")
print(f"hens' average weight is {round(avg_weight, 2)}")
print("hens' average weight is %.2f" % avg_weight)
print("hens' average weight is {:.2f}".format(avg_weight))
print("hens' average weight is {0:.2f}".format(avg_weight))

# 数据容器collection，是一种数据类型，它可以保存多个数据。
# 列表list，元组tuple，字符串str，字典set，集合dict
# 可迭代的数据类型有：列表、元组、字典、集合、字符串

# list 列表
# 列表可以放任意类型的数据，列表的元素可以重复，列表的元素可以改变
# 列表本身也是一个对象，列表的元素也是对象
list1 = [1, "two", "three", 4, 5, 6, 7, 8, 9, 10]
print(list1)
# 列表的遍历
for i in list1:
    print(i)
print("-----------------------------------------")
i = 0
while i < len(list1):
    print(list1[i])
    i += 1
# 可以定义空列表
list2 = []
list1 = list()
print(list2,type(list2))
print(list1,type(list1))
print("-----------------------------------------")
# 列表元素数据类型没有严格限制，允许重复，有序
list3 = [1, list1,list2]
list4 = [1, "two", "three", list3]
print(list4)
# 索引需要在列表的索引范围之内，否则会报错
print(list4[3][0])
# 通过.append（值）添加到序列的末尾
list3[0] = "超级无敌厉害"
print(list4)
list1.append("小飞侠")
print(list4)
# del 删除元素
del list1[0]
print(list4)
list1.append("小飞侠")
list1[0] = "消费者"
print(list4)
print("-----------------------------------------")
print(list4)
while len(list4) > 0:
    del list4[0]
    print(f"第{len(list4)}次删除的元素后：{list4}")

print("-----------------------------------------")

list1 = [1,2.1,"这是list1"]
print(f"list:{list1},地址:{id(list1)}")
print(f"list:{list1[2]},地址:{id(list1[2])}")
list1[2] = "这是list1修改后的值"
print(f"list:{list1},地址:{id(list1)}")
print(f"list:{list1[2]},地址:{id(list1[2])}")
list1[2] = "这是list1"
print(f"list:{list1},地址:{id(list1)}")
print(f"list:{list1[2]},地址:{id(list1[2])}")
# 列表依然存在内存驻留机制
print("------------------------------------------")
list2 = list1
print(f"list:{list2},地址:{id(list2)}")
list2[0] = 2
print(f"list:{list1},地址:{id(list1)}")
# 列表的相互赋值，不会产生内存驻留，会相互影响
print("------------------------------------------")
def f1(l):
    l[0] = 2
    print(f"函数f1()中l:{l},地址:{id(l)}")
list10 = [1,2,3]
print(f"list:{list10},地址:{id(list10)},list10[0]的地址:{id(list10[0])}")
f1(list10)
print(f"list:{list10},地址:{id(list10)},list10[0]的地址:{id(list10[0])}")
print("------------------------------------------")
# 列表的常用操作
print(f"list10:{list10}")
print(len(list10))
print(max(list10))
print(min(list10))
 # 将元组转为列表 list(seq)
print(f"2出现的次数:{list10.count(2)}")
# 将列表加入到原列表中
list10.extend([6,6,6])
print(f"list10:{list10}")
list1 = ["123456"]
list10.extend(list1)
print(f"list10:{list10}")
# 获取列表中某个元素的索引
print(list10.index(6)+1)
# 列表倒序
list10.reverse()
print(f"list10:{list10}")
# 插入数据
list10.insert(1,"小飞侠")
print(f"list10:{list10}")

# 列表生成式
# 语法格式为：[列表元素的表达式 for 自定义变量 in 可迭代对象]
list2 = [ele * 2 for ele in range(1,10)]
print(list2)
list3 = [ele + ele for ele in list2]
print(list3)
print([ele * ele for ele in range(1,11)])
scores = []
for i in range(5):
    scores.append(float(input(f"请输入第{i+1}个数:")))
print(scores)
