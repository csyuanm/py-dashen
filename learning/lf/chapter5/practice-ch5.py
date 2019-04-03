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