#coding=utf-8


#8.1 定义函数
print('****************')
print('8.1 定义函数')

def greeter_user():   #括号：在括号内指出函数为完成其任务需要什么信息；冒号：定义以冒号结尾。
    """显示简单的问候语"""    #文档字符串的注释，解释函数是做什么的
    print("Hello!")

greeter_user()


#8.1.1 向函数传递信息
print('****************')
print('8.1.1 向函数传递信息')

def greeter_user(username):   #通过在此添加username，就开让函数接受你给username指定的任何值
    """显示简单的问候语"""    #文档字符串的注释，解释函数是做什么的
    print("Hello!" + username.title() + "!")

greeter_user('jesse')


#在函数greeter_user()的定义中，变量username是一个形参
#在代码greeter_user('jesse')中，值是一个实参




















