#coding=utf-8

#4.1 遍历整个列表
print('****************')
print('4.1 遍历整个列表')

#4-1 比萨
pizzas = ['pepperoni','cheese','fruit']
for pizza in pizzas:
    print(pizza)

pizzas = ['pepperoni','cheese','fruit']
for pizza in pizzas:
    print("I love " + pizza + " pizza.")
print("I really love pizza!")


#4.3 创建数值列表
print('****************')
print('4.3 创建数值列表')


#4-3 数到20
for value in range(1,21):
    print(value)

#4-4 一百万
nums = list(range(1,1000001))
sum1=0
for value in nums:
    sum1 = sum1 + value
print(sum1)

#4-5 求和
print(sum(nums))

#4-6 奇数
odd_numbers = list(range(1,20,2))
print(odd_numbers)

#4-7 3的倍数
three = list(range(3,30,3))
for value in three:
    print(value)

#4-8 立方
cubes = []
for value in range(1,10):
    cubes.append(value**3)
for v in cubes:
    print(v)

#4-9 立方解析
cubes = [value**3 for value in range(1,10)]
print(cubes)

#4-10 切片
print('****************')
print('4-10 切片') 

players = ['charles','martina','michael','florence','eli']

print("The first three items in the list are:")
print(players[:3])
print(players[1:4])
print(players[-3:])

#4-11 你的比萨和我的比萨
my_pizzas = ['pepperoni','cheese','fruit']
friend_pizzas = my_pizzas[:]

my_pizzas.append('chocolate')
friend_pizzas.append('apple')

print("My favorite pizzas are:")
print(my_pizzas)

print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)

for my_pizza in my_pizzas:
    print(my_pizza)

for friend_pizza in friend_pizzas:
    print(friend_pizza)

#4-13 自助餐
foods = ('rice','noodles','cake','tea')

for food in foods:
    print(food)
    
foods = ('rice','noodles','rice noodle','water')

for food in foods:
    print(food)    








