"""
第五章 if语句（整合教科书（6-249行）及视频课程（253-末行））
"""
# 一、书本教程内容
# 5.1 简单if语句
cars = ['audi', 'volkswagen', 'subaru', 'nissan', 'toyota', 'geely', 'bmw', 'skoda', 'buick', 'chevrolet']
for car in cars:
    if car == 'geely':  # 如果遍历到的车厂为geely
        print(car.upper())  # 则字母全部大写
    else:  # 若不是geely
        print(car.title())  # 则首字母大写
# 条件测试(True & False)
car = 'geely'  # "="为赋值
car == 'geely'  # "=="为发问，car是否为geely.
print(car == 'geely')
# 此检验应考虑大小写
car = 'Geely'
car.lower() == 'geely'
print(car.lower() == 'geely')
# 检验相等
requesting = 'mushrooms'
if requesting != 'fish':
    print("here is the fish.")  # 因requesting的值不为fish，故执行if后代码print，若替换mushrooms为fish将返回false。
else:
    print("we have no the goods that you requesting.")
# 数学比较，判断范围
age = 19  # 下列各行运行时会显示true或false，Windows系统实现不了。

age < 21
print(age < 21)
age <= 21
print(age <= 21)
age > 21
print(age > 21)
age >= 21
print(age >= 21)
# 多条件判定(and,or)
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 <= 21
print(age_0 >= 21 and age_1 <= 21)
age_0 = 18
age_0 >= 21 or age_1 >= 21
print(age_0 >= 21 or age_1 >= 21)
# 检查特定值是否已包含在列表中（实例：注册账号时检验注册的用户名是否已被注册）----关键词： in 和 not in
requestings = ['mushrooms', 'onions', 'pineapple', 'cheese']
'onions' in requestings
print('onions' in requestings)
if 'onions' in requestings:
    print("yes,onions is added.")
else:
    print("please add onions!")
'pepperoni' in requestings
print('pepperoni' in requestings)

# 检查特定值是否不包含在列表中----关键词： not in
banned_users = ['link', 'lily', 'black']
'andrew' not in banned_users
print('andrew' not in banned_users)
if 'andrew' not in banned_users:
    print("you can post response if you wish.")

# 布尔表达式（判定游戏是否正在运行，用户是否可以编辑网站特定内容，跟踪程序状态等）
game_active = True
can_edit = False

# Practice 1
car = 'nissan'
print("is car == 'NISSAN'? I predict True")
print(car.upper() == 'NISSAN')
print("\ncar = 'audi'? I predict False")
print(car == 'adui')
# Practice 2
value1 = 21
value2 = 22
print(value2 == value1)
print(value1 >= 20 and value2 <= 30)
print(value1 <= 20 and value2 >= 100)
print(value1 > 10 or value2 < 23)
# Practice 3
cities = ['yujing', 'ruilin', 'qicang', 'wenyang', 'changxiu', 'xuanyun', 'tanchuan', 'yunji', 'linghan']
print('yinhuang' in cities)
print('changxiu' in cities)
if 'ninghai' not in cities:
    cities.insert(4, 'ninghai')
print(cities)

# if-else语句（判定到一个条件符合时终止，else可省略）
age = 20
if age >= 18:
    print("you are old enough to vote.")
    print("have you registered to vote yet?")
else:
    print("you are too young to vote!")

# if-else-elif语句（检查事件超过2个的情形,判定到一个条件符合时终止，else可省略）
age = 20
if age <= 4:
    print("free!")
elif age > 4 and age < 18:
    print("cost $5")
else:
    print("cost $10")  # 以下用简洁代码

"""
4 < age: free 
4 < age < 18: $5 
18 >= age: $10 
age > 65: $5 
"""
age = 20
if age <= 4:
    price = 0
elif age < 65:
    price = 10
else:
    price = 5
print("Your admission cost is $" + str(price) + ".\n")  # 该方法更简洁，但缺乏“人意”。

# if语句适合多个符合的条件(遇到符合条件的语句也会继续判定到末尾)
requesting = ['cheese', 'beef', 'squid', 'scallop', 'flounder']
if 'mushrooms' in requesting:
    print("add mushrooms")
if 'scallop' in requesting:
    print("add scallop")
if 'pork' in requesting:
    print("add pork")

# Practice 1  Page 76
alien_colors = ['green', 'yellow', 'red', 'purple']
for alien_color in alien_colors:
    if alien_color == 'green':
        print("well down,you got 5 points!")

# Practice 2
alien_colors = ['green', 'yellow', 'red']
for alien_color in alien_colors:
    if alien_color == 'yellow':
        print()
    else:
        print("perfect,you got 10 points!")
    if alien_color == 'red':
        print()
# Practice 3
alien_colors = ['green', 'yellow', 'red']
for alien_color in alien_colors:
    if alien_color == 'yellow':
        print("perfect!you got 10 points!")
    elif alien_color == 'green':
        print("well down!you got 5 points!")
    else:
        print("excllent!you got 20 points")
# Practice 4
age = 26
if age < 2:
    print("baby")
elif age < 4:
    print("b-chil")
elif age < 14:
    print("child")
elif age < 20:
    print("young man")
elif age < 65:
    print("adult")
else:
    print("old man")

# Practice 5
favorite_fruits = ['coconut', 'banana', 'pine']
if 'coconut' in favorite_fruits:
    print("Yes")
if 'apple' in favorite_fruits:
    print()
if 'pine' in favorite_fruits:
    print("Yes")
if 'banana' in favorite_fruits:
    print("hole yes!")
if 'orange' in favorite_fruits:
    print()

# if语句处理列表
drinks = ['pepsi', 'juice', 'sprite', 'fenta', 'hot coco']
for drink in drinks:
    if drink == 'sprite':
        print("sorry,the sprite is out of.")
    else:
        print("drink is preparing.")
"""
该方法可用于餐饮店内系统，告知顾客或店员库存情况。
系统管理员已做好库存变量赋值后的告知。
该方法做不到系统自行检查库存并报错，仍另需编程告知具体库存。
即 if 'sprite'为0时，print("sprite is out of.")
"""

# 检查列表是否为空
order_list = []
if order_list:
    for food in order_list:
        print("\nyour order is confirmed.")
else:
    print("please choose at least 1 food.")

# 对比列表（匹配为true，否则执行else）
"""
匹配顾客需求和店内供应
"""
available_requestings = ['beef', 'wine', 'duck', 'cookie', 'hamburger',
                         'fish', 'sashimi']
customs_requestings = ['apple', 'banana', 'pine', 'beef', 'cookie']
for requesting in customs_requestings:
    if requesting in available_requestings:
        print(requesting + " is already preparing.")
    else:
        print("we don't have " + requesting + ".")

# Practice 1 Page79 -80
names = ['admin', 'jesse', 'luke', 'aderson', 'hulk']
for name in names:
    if name == 'admin':
        print("Hello" + name + " would you like to see a status report?")
    else:
        print("Hello," + name + " thank you for logging in again.")
# Practice 2
names = []
if names:
    for name in names:
        if name == 'admin':
            print("Hello" + name + " would you like to see a status report?")
else:
    print("please type in a name.")
# Practice 3
current_users = ['jesse', 'luke', 'aderson', 'hulk', 'lawson']
new_users = ['jack', 'chen', 'yao', 'luke', 'HULK']
for user in new_users:
    if user.lower() in current_users:
        print(user + " is used.")
    else:
        print(user + " can be used.")
# Practice 4
numbers = list(range(1, 10))  # 第四章内容
for value in numbers:
    if value == 1:
        print("1st")
    elif value == 2:
        print("2nd")
    elif value == 3:
        print("3rd")
    else:
        print(str(value) + "th")

"""
二、视频教程内容
判断大小
例：判断 5000,2000,9000,1000的大小
"""
n0 = 5000
n1 = 2000
n2 = 9000
n3 = 1000
max_value = n0  # max_value是额外添加变量，变量不足时应记得添加变量
if n1 > n0:
    max_value = n1
if n2 > n1:
    max_value = n2
if n3 > n2:
    max_value = n3
print("MAX is " + str(max_value))
# 根据月份判断天数
month = int(input("month："))
if month < 1 or month > 12:
    print("Please tab correct numbers.(1-12)")
elif month == 2:
    print("28 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
else:
    print("31 days")

# 判断季节
season = input("season:")
if season == "春":
    print("February,March,April")
elif season == "夏":
    print("May,June,July,August")
elif season == "秋":
    print("September,October")
elif season == "冬":
    print("November,December,January")
else:
    print("it's not the current  earth seasons.")

# 根据运算符计算两个数字。录入数字和运算符，试写出若运算符不是“+ - * /”任意一个，则提示“运算有误”，若是其中一个运算符请print运算结果的代码
number1 = int(input("number1:"))
number2 = int(input("number2:"))
opreator = input("opreator:")
if opreator == "+":
    value = number1 + number2
    print(value)
elif opreator == "-":
    value = number1 - number2
    print(value)
elif opreator == "*":
    value = number1 * number2
    print(value)
elif opreator == "/":
    value = number1 / number2
    print(value)
else:
    print("error:please check number and opreator.")

# 练习1
month = int(input("month:"))
if month < 1 or month > 12:
    print("incorrect type.")
elif month == 1 or month > 10:
    print("冬")
elif month >= 9:
    print("秋")
elif month >= 5:
    print("夏")
else:
    print("春")
# 练习2
years = int(input("年龄:"))
if years < 0:
    print("错误")
elif years < 2:
    human = "婴儿"
elif years < 13:
    human = "儿童"
elif years < 20:
    human = "青年"
elif years < 65:
    human = "成年"
elif years <= 150:
    human = "老年"
else:
    print("it's not possible!")
print(human)

# 练习3
tall = float(input("身高:"))
weight = float(input("体重:"))
BMI = (tall / weight) ** 2
if BMI < 18.5:
    health = "偏瘦"
elif BMI < 24:
    health = "正常"
elif BMI < 28:
    health = "超重"
elif BMI < 30:
    health = "I度肥胖"
elif BMI < 40:
    health = "II度肥胖"
else:
    health = "III度肥胖"
print(health)
# 可改写为高级形式： "偏瘦" if MNI<18.5 else "肥胖"（本改法为示例，不适用本练习内容）
numbers = list(range(3, 11))
for value in numbers:
    if value > 3 and value < 10:
        print(value)
