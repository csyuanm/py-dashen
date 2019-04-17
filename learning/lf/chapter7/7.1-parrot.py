#coding=utf-8


def add(a, b):
    sum = float(a)+ float(b)
    print('两数相加=' + str(sum))

#7.1 函数input()的工作原理 
print('****************')
print('7.1 函数input()的工作原理')
a=0
#函数input()让程序暂停运行，等待用户输入一些文本。获取用户之后，将其存储到一个变量中，以方便使用。
#input()接受一个参数：即要向用户显示的提示或者说明，让用户知道该如何做
message = input('Tell me something, and I will repeat it back to you: ')
print(message)
a = input('请输入一个数字: ')         #  '6'   temp = 6(用户输入的内容)  -》 str(temp)
b = input('请输入第二个数字: ')
add(a, b)


#7.1.1 编写清晰的程序

name = input("Please enter your name: ")
print("Hello, " + name + "!")




