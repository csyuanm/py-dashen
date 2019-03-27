#coding=utf-8

#4.4 使用列表的一部分
print('****************')
print('4.4 使用列表的一部分')

#4.4.1 切片【处理列表的部分元素】
print('****************')
print('4.4.1 切片')

players = ['charles','martina','michael','florence','eli']
print(players[0:3])     #包含索引为0-2的三名队员
print(players[1:4])     #包含索引为1-3的三名队员

players = ['charles','martina','michael','florence','eli']
print(players[:4])     #如果没有指定第一个索引，则自动从列表开头开始

players = ['charles','martina','michael','florence','eli']
print(players[2:])     #如果没有指定最后一个索引，则切片终止于列表末尾

players = ['charles','martina','michael','florence','eli']
print(players[-3:])     #输出名单上最后三个队员


#4.4.2 遍历切片【可在for循环使用切片】
print('****************')
print('4.4.2 遍历切片')

players = ['charles','martina','michael','florence','eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
    

 #4.4.3 复制列表
print('****************')
print('4.4.3 复制列表')  

#复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]   #复制整个列表：同时省略起始索引和终止索引

print('My favorite foods are:')
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')   #每个列表添加一种食品
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#简单的赋值
#简单地将my_foods赋给friend_foods，而不是将my_foods的副本存储到friend_foods，就不能得到两个列表
#这种语法实际上是将新变量friend_foods关联到包含在my_foods中的列表，因此这两个变量都指向同一个列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods   

my_foods.append('cannoli')  
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)




