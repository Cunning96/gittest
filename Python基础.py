"""
第二章 基础

name = name.rstrip()
name = name.lstrip()
name = name.strip()
id()    查看变量地址是否一致
"""
# 单行注释以#开始，多行注释以"""开头，"""结尾。

# 多行注释举例：
"""
1是数字
a是字母
甲是汉字
"""

# 为语句设置字母大小写
first_name = 'Eric'
last_name = 'Matthes'
full_name = first_name + " " + last_name
print(full_name.upper())  # 所有字母大写
print(full_name.lower())  # 所有字母小写
print(full_name.title())  # 首字母大写
print("Hello," + full_name.title() + "," + "I'm Cunning.")

# 删除空白区域
name = 'eric '
name = name.rstrip()
name
name = ' eric'
name = name.lstrip()
name
name = ' eric '
name = name.strip()
name

#检验变量id地址（只适用于文件式节省内存，并不适用于交互式）
a = 800
b = 10000
print(id(a))
print(id(b))
print(a is not b)
c = a
print(a is c)
d = 800
print(id(d) is not id(a))    # 两个值一样的变量可以整合节省内存

"""
视频课内容
result +=     累进计算（见20-30行）
计算4位数求和
例1：1234每位求和
方法1.
"""
# 个位，1234除以10的余数
number = 1234
unit0 = number%10
# 十位，1234除以10的商，再除以10之后的余数
unit1 = number//10%10
# 百位 1234除以100的商，再除以10的余数
unit2 = number//100%10
# 千位，1234除以1000的余数
unit3 = number//1000
summation = unit0+unit1+unit2+unit3
print("result is "+ str(summation))

"""
计算4位数求和
例1：1234每位求和
方法2.（result +，累进迭代）
"""
number = 1234
result = number%10
result += number//10%10
result += number//100%10
result += number//1000
print("result is "+ str(result))