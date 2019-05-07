#coding=utf-8

#7.2.2 让用户选择何时退出

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""      #初始值为一个空白字符串，让python能够执行while循环所需的比较
while message != 'quit':
    message = input(prompt)  #只要message的值不是'quit'，这个循环就会不断运行
    print(message)


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""      #初始值为一个空白字符串，让python能够执行while循环所需的比较
while message != 'quit':
    message = input(prompt)  #只要message的值不是'quit'，这个循环就会不断运行
    
    if message != 'quit':    #仅在消息不是退出值时才打印它
        print(message)


#7.2.3 使用标志
print('****************')
print('7.2.3 使用标志')

#在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。这个变量被称为标志。

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)
    
    if message != 'quit':
        print(message)
    else:
        active = False




















        
    