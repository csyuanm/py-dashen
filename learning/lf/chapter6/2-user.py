#coding=utf-8

#6.3 遍历字典


#6.3.1 遍历所有的键-值对
print('****************')
print('6.3.1 遍历所有的键-值对')

user_0= {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

#声明两个变量key和value，用于存储键-值对中的键和值
#for语句的第二部分包含字典名和方法items()
for key,value in user_0.items():   
    print("\nKey: " + key)
    print("Value: " + value)


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")


#6.3.2 遍历字典中的所有键【方法keys()】
print('****************')
print('6.3.2 遍历字典中的所有键')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',
    }

#使用方法keys()的键遍历
for name in favorite_languages.keys():   
    print(name.title())

#不使用使用方法keys()的键遍历，因为遍历字典时，会默认遍历所有的键
for name in favorite_languages:   
    print(name.title())


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():     #注意此处for语句与if循环的关系
    print(name.title())
    
    if name in friends:
        print("  Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")   #为访问喜欢的语言，把name作为当前值作为键！！！！？？？？

#使用keys()确定某人是否接受了调查
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',
    }

if 'erin' not in favorite_languages.keys():
    print("Erin, please take out poll!")


#6.3.3 遍历字典中的所有值【方法values()】
print('****************')
print('6.3.3 遍历字典中的所有值')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():   #使用values()遍历字典中的所有值，但未考虑重复
    print(language.title())


#使集合set，可剔除所提取的字典中的值的重复项
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'phil': 'python',
    'edward': 'ruby',
    }

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):   #使用set()找出列表非重复项，并用这些元素创建一个集合
    print(language.title())








