#coding=utf-8


def add(a, b):
    sum = float(a)+ float(b)
    print('两数相加=' + str(sum))

#7.1 函数input()的工作原理 
print('****************')
print('7.1 函数input()的工作原理')

#函数input()让程序暂停运行，等待用户输入一些文本。获取用户之后，将其存储到一个变量中，以方便使用。
#input()接受一个参数：即要向用户显示的提示或者说明，让用户知道该如何做

a = input('请输入一个数字: ')         #  '6'   temp = 6(用户输入的内容)  -》 str(temp)
b = input('请输入第二个数字: ')
add(a, b)

message = input('Tell me something, and I will repeat it back to you: ')
print(message)


#7.1.1 编写清晰的程序
print('****************')
print('7.1.1 编写清晰的程序')

name = input("Please enter your name: ")
print("Hello, " + name + "!")


#创建多行字符串
prompt = "If you tell us who you are, we can personalize the messages you see."  #第1行将消息的前半部分存储在变量prompt中
prompt += "\nWhat is your first name?"  #第2行中，运算符+=在存储在prompt中的字符串末尾附加一个字符串

name = input(prompt)
print("\nHello, " + name + "!")


#7.1.2 使用int()来获取数值输入
print('****************')
print('7.1.2 使用int()来获取数值输入')

age = input("How old are you?")
print(age)   #此处显示的数字为字符串


age = input("How old are you?")
age = int(age)
print(age) 


height = input("How old are you, in inches?")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")



























