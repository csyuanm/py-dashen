

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
#要判断两个值是否不相等，课结合使用表示“不等”的“！=”

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")


#5.2.4 比较数字
#条件语句中可包含各种数学比较，比如<, <=, >, >=

answer = 17
if answer != 42:
    print("That is not the correct answer. Please Try again!")













