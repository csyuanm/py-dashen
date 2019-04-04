#coding=utf-8

#5.4 使用if语句处理列表
print('****************')
print('5.4 使用if语句处理列表')

#5.4.1 检查特殊元素
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

#比萨店青椒用完了 --可在for循环中包含一条if语句
requested_toppings = ['mushrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

#5.4.2 确定列表不是空的
requested_toppings = []

#在if语句中将列表名用在条件表达式时，将在列表至少包含一个元素时返回True，并在列表为空时返回False。
if requested_toppings:  #进行了简单检查，而不是直接用for循环
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")


#5.4.4 使用多个列表

available_toppings = ['mushrooms','olives','green peppers',
                      'pepperoni','pineapple','extra cheese']  #供应的配料固定，可用元组来存储

requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:  #遍历顾客点的配料列表
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")


