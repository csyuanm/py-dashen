#coding=utf-8

#3.1 列表是什么
print('****************')
print('3.1 列表是什么')

#3-1 姓名
names = ['Jack','Tom','Susan','Alice']
print(names[0])
print(names[1])
print(names[2])
print(names[-1])

#3-2 问候语
message = "How are you going, " + names[0] + "?"
print(message)

for i in names:
    print("How are you going, " + i + "?")
    
#3-3 自己的列表
vehicles = ['bike','motorcycle','bus','car']
message = "I would like to own a Honda " + vehicles[1] + "."
print(message)





