

#5.1 一个简单示例
print('****************')
print('5.1 一个简单示例')

cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
    

#5.2 条件测试
#条件测试：条件测试的值为True，则执行if语句后面的代码；若为False，则忽略这些代码。
print('****************')
print('#5.2 条件测试')

#5.2.1 检查是否相等
#使用相等运算符（==）来检查两个值是否相等，如果相等则返回True，否则返回False。
#一个等号（=）是陈述；两个等号（==）是发问。
#car = 'bmw'
#car == 'bmw'
#返回True

#car = 'bmw'
#car == 'audi'
#返回False

#5.2.2 检查是否相等时不考虑大小写
#（1）在Python中检查是否相等时如果区分大小写，则两个大小写不同的值会视为不相等
#car = 'Audi'
#car == 'audi'
#返回False

#（2）如果大小写无关紧要，只想检查变量的值，可根据拿来做比较的值的大小写情况，将被检查的变量的值进行大小写转换
#car = 'Audi'
#car.lower() == 'audi'
#返回True


#5.2.3 检查是否不相等
#要判断两个值是否不相等，可结合使用表示“不等”的“！=”

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")


#5.2.4 比较数字
#条件语句中可包含各种数学比较，比如<, <=, >, >=

answer = 17
if answer != 42:
    print("That is not the correct answer. Please Try again!")


#5.2.5 检查多个条件（关键字and和or）
#1.使用and检查多个条件（要检查两个条件是否都为True，可用and)

#age_0 = 22
#age_1 = 18
#age_0 >= 21 and age_1 >= 21
#False

#age_0 = 22
#age_1 = 22
#age_0 >= 21 and age_1 >= 21
#True

#或：（age_0 = 21）and (age_1 = 21)

#2.使用or检查多个条件（至少一个条件满足则为Tru；两个条件都不满足则为False)

#age_0 = 22
#age_1 = 18
#age_0 >= 21 or age_1 >= 21
#True

#age_0 = 18
#age_0 >= 21 0r age_1 >= 21
#False


#5.2.6 检查特定值是否在列表中

#requested_toppings = ['mushrooms','onions','pineapple']
#'mushrooms' in requested_toppings
#True

#'pepperoni' in requested_toppings
#False

#5.2.7 检查特定值是否不在列表中（关键字not in)

banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")


#5.2.8 布尔表达式（条件测试的别名）















