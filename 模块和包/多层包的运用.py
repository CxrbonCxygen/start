# @Version : 1.0
# @Auther : CarbonOxygen
# @File : 多层包的运用.py
# @Time : 2026/4/4 11:51
from math import fabs

# 方法1
import c_package.c_pakeage2.moduel03
c_package.c_pakeage2.moduel03.cal(2, 3)

# 方法2
from c_package.c_pakeage2.moduel03 import cal
cal(3, 3)

# 方法3
from c_package.c_pakeage2 import moduel03
moduel03.cal(4, 4)

# 快捷键
# alter + enter 是给你解决方案
print(fabs(-12.6))