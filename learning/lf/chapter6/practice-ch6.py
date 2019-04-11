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


#6.4 嵌套
print('****************')
print('6.4 嵌套 ')

#6-7 人
name_1 = {'first_name':'Nancy', 'last_name':'Smith', 'age':26, 'city':'Wuhan'}
name_2 = {'first_name':'Luis', 'last_name':'Merilan', 'age':24, 'city':'Beijing'}
name_3 = {'first_name':'Jack', 'last_name':'Tomson', 'age':25, 'city':'Nanjing'}

people = [name_1, name_2, name_3]

for name in people:
    print(name)

#6-8 宠物
print('6-8 宠物 ')

Mimi= {'type': 'cat', 'owner': 'Eric'}
Wangwang = {'type': 'dog', 'owner': 'Amanda'}
Gilly = {'type': 'bird', 'owner': 'Nana'}

pets = [Mimi, Wangwang, Gilly]

for pet in pets:
    print("It's a " + pet['type'] + " of " + pet['owner'] + ".")


#6-9 喜欢的地方
print('6-9 喜欢的地方 ')

favorite_places = {
        'Frank': ['China', 'Japan'],
        'Susan':['Japan'], 
        'Eric': ['Finland','New Zealand'],
                       }

for name, places in favorite_places.items():
    if len(places) > 1:
        print("\n" + name + "'s favorite places are:")
        
        for place in places:  
            print("\t" + place)
    
    else:
        print("\n" + name + "'s favorite places is " + places[0] + ".")
        

#6-10 喜欢的数字
print('6-10 喜欢的数字')

favorite_numbers = {
    'Lucy':[5,7,9],
    'Smith':[4,8,9],
    'Eric':[0,1,5],
    'Mona':[2,8],
    'Lily':[6,8],
    }


for name, numbers in favorite_numbers.items():
    print("\n" + name + "'s favorite numbers are:")
                
    for number in numbers:  
        print("\t" + str(number))

#6-11 城市
print('6-11 城市')

cities = {
    'Guangzhou':{
        'country':'China',
        'population': 17,
        'fact': 'It locates in South of China.'
        },
    
    'Tokyo':{
        'country':'Japan',
        'population': 20,
        'fact': 'It is the national capital of Japan.'
    },
    
    'Los Angeles':{
        'country':'America',
        'population': 15,
        'fact': 'It is a  prosperous city.'
    },
    
    }

for city, information in cities.items():
    print("\n" + city + "'s information:")
                    
    print("Country: " + information['country'] + ".")
    print("Population: " + str(information['population']) + " million.")
    print("Fact: " + information['country'])











