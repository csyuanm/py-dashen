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


#创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#显示前五个外星人
for alien in aliens[:5]:
    print(alien)

print('...')








