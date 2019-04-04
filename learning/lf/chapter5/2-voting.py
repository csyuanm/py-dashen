#coding=utf-8

#5.3 if语句
print('****************')
print('5.3 if语句')

#5.3.1 简单的if语句

#最简单的if语句只有一个测试和一个操作：
#if conditional_test:
    #do something（若测试结果为True，则执行紧跟if语句后面的代码；结果为False，则不执行）

age = 19
if age >= 18:
    print("You are old enough to vote!")

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you redistered to vote yet?")


#5.3.2 if-else语句

#通常需要在条件测试通过时执行一个操作，在没有通过时执行另一个操作。可使用if-else语句。

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you redistered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote asd soon as you turn 18!")


#5.3.3 if-elif-else结构（检查超过两个的情况）
#仅适用于只有一个条件满足的情况

#Python只执行结构中的一个代码块，它一次检查每个条件测试，直到遇到通过了的条件测试。
#测试通过后，执行紧跟在它后面的代码，并跳过余下的测试。

age= 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

age= 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")


#5.3.4 使用多个elif板块（可根据需要使用任意数量的elif板块）

age= 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10    
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")


#5.3.5 省略else代码块

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10  
elif age >= 65:
    price = 5 

print("Your admission cost is $" + str(price) + ".")


#5.3.6 测试多个条件

requested_toppings = ['mushrooms','extra cheese'] #三个if测试独立存在

if 'mushrooms' in requested_toppings:  #检查顾客是否点了“mushrooms”
    print("Adding mushrooms.")
if 'pepproni' in requested_toppings:   #不管前一个测试是否通过，都将进行这个测试
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:  #不管前两个测试的结果如何，都将进行这个测试
    print('Adding extra cheese.')

print("\nFinished making your pizza!")












