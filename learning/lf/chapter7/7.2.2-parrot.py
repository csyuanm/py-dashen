#coding=utf-8

#7.2.2 让用户选择何时退出

#1)单词quit也打印出来
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""      #初始值为一个空白字符串，让python能够执行while循环所需的比较
# while message != 'quit':
#     message = input(prompt)  #只要message的值不是'quit'，这个循环就会不断运行                                                                                          
#     print(message)

#2)使用一个if测试，使得单词quit不打印出来
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""      #初始值为一个空白字符串，让python能够执行while循环所需的比较
while message != 'quit':
    message = input(prompt)  #只要message的值不是'quit'，这个循环就会不断运行
     
    if message != 'quit':
        print(message)

    if message == 'a':
        message = 'quit'



#7.2.3 使用标志
print('****************')
print('7.2.3 使用标志')

#在需要很多条件都满足才能继续运行的程序中，可定义一个变量（即标志），用于判断程序是否处于活动状态
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    elif message == 'exit':
        active = False
    else:
        print(message)    
        


















        
    