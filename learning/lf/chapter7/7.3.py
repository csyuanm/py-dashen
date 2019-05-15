#coding=utf-8
from itertools import repeat


#7.3 使用while循环来处理列表和字典

#要在遍历列表的同时对其进行修改，可使用while循环。


#7.3.1 在列表之间移动元素
print('****************')
print('7.3.1 在列表之间移动元素')

#首先，创建一个待验证用户列表
#和一个用于存储已验证用户的空列表

unconfirm_users = ['alice', 'brain', 'candace']
confirm_users = []

#验证每个用户，直到没有未验证用户为止
#将每个经过验证的列表都移到已验证用户列表中

while unconfirm_users:
    current_user = unconfirm_users.pop()    #函数pop()以每次一个的方式从列表unconfirm_users末尾删除未验证用户
    
    print("Verifying user: "+ current_user.title())
    confirm_users.append(current_user)

#显示所有已验证用户
print("\nThe following users have been confirmed:")
for confirm_user in confirm_users:
    print(confirm_user.title())


#7.3.2 删除包含特定值的所有列表元素
print('****************')
print('7.3.2 删除包含特定值的所有列表元素')

#函数remove()可用来删除列表中的特定值，但是它只删除第一次出现在列表的该值；如果要删除列表中包含所有特定值的元素，需用while循环。

pets = ['dog', 'cat', 'dog', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)


#7.3.3 使用用户输入来填充字典
print('****************')
print('7.3.3 使用用户输入来填充字典')

responses = {}

#设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    
    #将答卷存储在字典中
    responses[name] = response
    
    #看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond?(Yes/ no) ")
    if repeat == "no":
        polling_active = False
        
    #调查结束，显示结果
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(name + "would you like to climb " + response + ".")
    
    
    
    
    








             







