#coding=utf-8

#6.4.2 在字典中存储列表
print('****************')
print('6.4.2 在字典中存储列表')

#存储所点披萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],    #需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表
    }

#概述所点的披萨
print("You odered a " + pizza['crust'] + "-crust pizza " + 
      "with the  following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)
    

print('------键-值中列表含多个元素--------')    
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'phil': ['python', 'haskell'],
    'edward': ['ruby', 'go']
    }

#在遍历该字典的for循环中，需要再使用一个for循环来遍历与被调查者相关联的语言列表：
for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


#在遍历该字典的for循环中，需要再使用一个for循环来遍历与被调查者相关联的语言列表：
print('------for循环字典时使用if语句---------')

for name,languages in favorite_languages.items():
    if len(languages) > 1 :
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    else:
        print(name.title() + "'s favorite language is " + languages[0].title() + ".")


#6.4.3 在字典中存储字典
print('****************')
print('6.4.3 在字典中存储字典')

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'aeinstein',
        'location': 'princeton',
        },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris', 
        },
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tlocation: " + location.title())






















    
    