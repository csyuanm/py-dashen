#coding=utf-8

#4.1 遍历整个列表
print('****************')
print('4.1 遍历整个列表')

#需要对列表中的每个元素都执行相同的操作时，可使用for循环

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magicians)
    
#4.1.2 在for循环中执行更多的操作
print('****************')
print('4.1.2 在for循环中执行更多的操作')  

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!') 

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ', that was a great trick!') 
    
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!") 
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    
#4.1.3 在for循环结束后执行一些操作
#在for循环后面，没有缩进的代码都只执行一次
print('****************')
print('4.1.3 在for循环结束后执行一些操作') 

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")  #开头两个print语句对列表中的每个魔术师执行
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!") #第三个print语句没有缩进，因此只执行一次


#4.2 避免缩进错误
#Python根据【缩进】来判断代码行与前一个代码行的关系
print('****************')
print('4.2 避免缩进错误')

#4.2.1 缩进错误1：忘记缩进
print('****************')
print('4.2.2 缩进错误1：忘记缩进')

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician)

#4.2.2 缩进错误2：忘记缩进额外的代码行
print('****************')
print('4.2.3 缩进错误2：忘记缩进额外的代码行')

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!") 
print("I can't wait to see your next trick, " + magician.title() + ".\n")  #没有缩进，因此它只在循环结束后执行一次。

#4.2.3 缩进错误3：不必要的缩进

#4.2.4 缩进错误4：循环后不必要的缩进
print('****************')
print('4.2.3 缩进错误2：忘记缩进额外的代码行')

magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!") 
    print("I can't wait to see your next trick, " + magician.title() + ".\n") 
    print("Thank you, everyone. That was a great magic show!")  #因为缩进，它将针对列表中的每位魔术师执行一次

#4.2.5 缩进错误5：遗漏了冒号


