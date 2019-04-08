#coding=utf-8

#6.1 一个简单的字典【字典：一系列键-值对，用放在{}中的一系列键-值对表示】
#键-值对为两个相关联的值
print('****************')
print('6.1 一个简单的字典')

alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])


#6.2 使用字典
print('****************')
print('6.2 使用字典')

#6.2.1 访问字典中的值
print('****************')
print('6.2.1 访问字典中的值')

alien_0 = {'color':'green'}   
print(alien_0['color'])    #要获取与键相关联的值，可依次指定字典名和放在方括号内的键

alien_0 = {'color':'green','points':5}

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")


#6.2.2 添加键-值对
print('****************')
print('6.2.2 添加键-值对')

alien_0 = {'color':'green','points':5}
print(alien_0)

alien_0['x_position'] = 0    #新增键-值对，键为'x_position'，值为0
alien_0['y_position'] = 25   #新增键-值对，键为'y_position'，值为25
print(alien_0)


#6.2.3 先创建一个空字典（在空字典中添加键-值对）
print('****************')
print('6.2.3 先创建一个空字典')

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)


#6.2.4 修改字典中的值
print('****************')
print('6.2.4 修改字典中的值')

alien_0 = {'color':'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print("Original x_position: " + str(alien_0['x_position']))

#向右移动外星人
#据外星人当前速度决定其移动多远（使用if-elif-else结构，并存储在变量x_increment中）

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3    #这个外星人的速度一定很快

#新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New_position: " + str(alien_0['x_position']))


#6.2.5 删除键-值对【使用del语句，删除的键-值对永远消失】
print('****************')
print('6.2.5 删除键-值对')

alien_0 = {'color':'green','points':5}
print(alien_0)

del alien_0['points']  #使用del语句时，必须hiding字典名和要删除的键
print(alien_0)  #键'points'及其值5已从字典中删除


#6.2.6 由类似对象组成的字典
print('****************')
print('6.2.6 由类似对象组成的字典')

#前面的示例中，字典是存储一个对象的多种信息；其实也可存储多个对象的同一种信息
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',
    }

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")












