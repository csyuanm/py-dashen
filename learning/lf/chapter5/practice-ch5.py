#coding=utf-8

#5.1与5.2
print('****************')
print('5.1与5.2')

#5-1 条件测试
car = 'sabaru'
print("Is car == 'subaru'? I predict it True.")
print(car == 'subaru')

#5-2 更多的测试
name = 'David'
print(name == 'David')
print(name == 'david')
print(name.lower()=='david')

#round_1 = 14
#round_2 = 12
#round_1 >=13 and round_2 >=13

foods = ['rice','fruits','meat']
#'rice' in foods

food = 'milk'
if food not in foods:
    print("I don't like Milk.")
    
#5.3
print('****************')
print('5.3')    

#5-3 外星人颜色-1

alien_color = 'green'

if alien_color == 'green':
    print("The playist gets 5 points.") 
    
if alien_color != 'green':
    print('Not found.')   


#5-4 外星人颜色-2

#版本1
alien_color = 'green'

if alien_color == 'green':
    print("The playist gets 5 points.")
    
#版本2
alien_color = 'blue'

if alien_color == 'green':
    print("The playist gets 5 points.")
else:
     print("The playist gets 10 points.")


#5-5 外星人颜色-3

age = 15

if age < 2:
    print("He is a baby.")

elif age < 4:
    print("He is learning to walk.")
    
elif age < 13:
    print("He is a child.")

elif age < 20:
    print("He is a teen.")
    
elif age < 65:
    print("He is an adult.")    
    
else:
    print("He is an old man.")


#5-7 喜欢的水果
favorite_fruits = ['apple','strawberry','banana']

if 'apple' in favorite_fruits:
    print("You really like apple!")

if 'strawberry' in favorite_fruits:
    print("You really like strawberry!")

if 'banana' in favorite_fruits:
    print("You really like banana!")

if 'pineapple' in favorite_fruits:
    print("You really like pineapple!")


#5.4
print('****************')
print('5.4')    

#5-8 以特殊方式跟管理员打招呼

user_names = ['david','admin','susan','alice','tom']

for user_name in user_names:
    if user_name == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + user_name.title() + ', ' + "thank you for logging again.")

#5-9 处理没有用户的情形
user_names = []
if user_names:
    for user_name in user_names:
         print("Hello " + user_name.title() + ', ' + "thank you for logging again.")
else:
    print("We need to find some users!")

#5-10 检查用户名
current_users = ['david','amber','susan','alice','tom']

new_users = ['Jack','tom','macheal','david','Julia']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("Please put in another name.")
    else:
        print("This name is not occupied.")

#5-11 设置if语句的格式
numbers = list(range(1,10))

for value in numbers:
    print(value)

for value in numbers:
    if value == 1:
        print("1st")
    elif value == 2:
        print("2nd")
    elif value == 3:
        print("3rd")
    else:
        print(str(value) + "th")
    