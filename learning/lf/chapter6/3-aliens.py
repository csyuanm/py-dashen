#coding=utf-8

#6.4 嵌套
#列表中嵌套字典，或字典中嵌套列表，或字典中嵌套字典


#6.4.1 字典列表
print('****************')
print('6.4.1 字典列表')

alien_0 = {'color': 'green', 'points': 5}  #首先创建三个字典
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]   #将字典都放在一个列表中

for alien in aliens:   #遍历列表，将每个外星人都打印出来
    print(alien)

#1.使用range()生成多个外星人
print('****************')
print('使用range()生成多个外星人')

#创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):   #range()返回一系列数字，告诉python要重复这个循环多少次
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}   #每次执行循环，都创建一个外星人
    aliens.append(new_alien)    #并将其附加到列表aliens的末尾

#显示前五个外星人
for alien in aliens[:5]:
    print(alien)

print('...')

#显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))

#2.修改多个外星人的信息
print('****************')
print('修改多个外星人的信息')

#创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':   #alien['color']：针对alien而言
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
        
#显示前五个外星人
for alien in aliens[0:5]:
    print(alien)
print('...')    


#3.使用elif代码块
print('****************')
print('使用elif代码块')

#创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
#显示前五个外星人
for alien in aliens[0:5]:
    print(alien)
print('...')    
















