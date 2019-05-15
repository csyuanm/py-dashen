#coding=utf-8

#7.2 while循环简介

#7-4 比萨配料
# prompt = "What kind of topping would you like?"
# 
# topping = ''
# while topping != 'quit':
#     topping = input(prompt)
#     print("We will add " + topping.title() + " into the pizza!")


#7-5 电影票
# prompt = "Please input your age:"
# age = 0
# while age != -1:
#     age = int(input(prompt))
#        
#     if 0 < age < 3:
#         print("The ticket is free.")
#     elif 3 <= age < 12:
#         print("The price is 10 dollars.")    
#     elif age >= 12:
#         print("The price is 15 dollars.")
    
    #7-6-1
#     else:
#         flag = False
            
    
    #7-6-2
# flag = True
# 
# while flag:
#     age = int(input(prompt))
#        
#     if 0 < age < 3:
#         print("The ticket is free.")
#     elif 3 <= age < 12:
#         print("The price is 10 dollars.")    
#     elif age >= 12:
#         print("The price is 15 dollars.")    
#     
#     else:
#         flag = False
        
        
    #7-6-3
        
prompt = "Please input your age:"
  
while True:
    age = input(prompt)
    
    if age == 'quit':
        break 
      
    if 0 < int(age) < 3:
        print("The ticket is free.")
    elif 3 <= int(age) < 12:
        print("The price is 10 dollars.")    
    elif int(age) >= 12:
        print("The price is 15 dollars.")        
    else:
        print("不支持该类型输入，请重新输入年龄。")   





            






































     
    
    
    
    
        
        
