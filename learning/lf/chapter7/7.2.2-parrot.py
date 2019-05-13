#coding=utf-8

#7.2.2 让用户选择何时退出

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""      #初始值为一个空白字符串，让python能够执行while循环所需的比较
# while message != 'quit':
#     message = input(prompt)  #只要message的值不是'quit'，这个循环就会不断运行
#     print(message)


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

message = ""      #初始值为一个空白字符串，让python能够执行while循环所需的比较
while message != 'quit':
    message = input(prompt)  #只要message的值不是'quit'，这个循环就会不断运行
     
    if message != 'quit':
        print(message)

    if message == 'a':
        message = 'quit'




















        
    