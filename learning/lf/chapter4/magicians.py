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
    
for i in range(1,10):
    for j in range(1, i):
        print(str(j) + '*' + str(i) +'=' + str(i*j))









 