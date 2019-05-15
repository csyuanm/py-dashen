#coding=utf-8


#7.2.5 在循环中使用continue
print('****************')
print('7.2.5 在循环中使用continue')

#要返回到循环开头，并且根据条件测试结果决定是否继续执行循环，可使用continue语句

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:   #如果模为0，则执行continue语句，忽略余下的代码，返回循环开头
        continue
    
    print(current_number)    #如果当前数字不能被2整除，则执行循环中的余下代码，将该数字打印出来
    

#7.2.6 避免无限循环
print('****************')
print('7.2.6 避免无限循环')

x = 1
while x <= 5:
    print(x)
    
    x += 1







