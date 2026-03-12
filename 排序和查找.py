# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 排序和查找.py
# @Time : 2026/3/12 10:57

# 排序的列表
# 冒泡排序
list1 = [5, 4, 3, 2, 1]
for j in  range(len(list1) - 1):
    for i in range(len(list1) - j - 1 ):
        if list1[i] > list1[i + 1]:
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
    print(f"第{j+1}轮排序：{list1}")

# 二分查找
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]