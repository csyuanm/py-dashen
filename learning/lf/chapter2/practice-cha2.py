#coding=utf-8
#2-3 个性化消息
user_name='Eric'
print("Hello "+user_name+", "+"would you like to learn some Python today?")

#2-4 调整名字的大小写
name='Tom smith'
print(name.lower())
print(name.upper())
print(name.title())

#2-5 名言
name='Albert Einstein'
print(name+' once said, '+'"A person who ever made a mistake never tried anything new.')

#2-7 剔除人名中的空白
name='\tAlbert Einstein\n'
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())