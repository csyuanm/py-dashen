#coding=utf-8

#6.1和6.2 
print('****************')
print('6.1n6.2')

#6-1 人
name = {'first_name':'Nancy', 'last_name':'Smith', 'age':26, 'city':'Wuhan'}
print(name['first_name'])
print(name['last_name'])
print(name['age'])
print(name['city'])

#6-2 喜欢的数字

numbers = {
    'Lucy':5,
    'Smith':16,
    'Eric':1,
    'Mona':8,
    'Lily':6}
print("Lucy's favorite number is " + str(numbers['Lucy']) + ".")
print("Smith's favorite number is " + str(numbers['Smith']) + ".")
print("Eric's favorite number is " + str(numbers['Eric']) + ".")
print("Mona's favorite number is " + str(numbers['Mona']) + ".")
print("Lily's favorite number is " + str(numbers['Lily']) + ".")


#6.3 遍历字典 
print('****************')
print('6.3 遍历字典 ')

#6-5 河流
rivers = {'nile':'egypt',
          'mississippi':'america',
          'yangzi':'china',
          }

for river,country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
    
for river in rivers.keys():
    print(river.title())   
    
for country in rivers.values():
    print(country.title())    
    
#6-6 调查
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',
    }    

propable_names = ['franc', 'jen', 'jessica', 'edward']

for name in favorite_languages.keys():
    if name in propable_names:
        print(name.title() + ", thank you for supporting the investigation.")
    else:
        print(name.title() + ', please jion our investigation.')


