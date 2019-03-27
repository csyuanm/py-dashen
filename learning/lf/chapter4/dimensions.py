#coding=utf-8

#4.5 元组【不能修改的值称为不可变的，而不可变的列表称为元组（对应的，列表是可变、可修改的）】 
print('****************')
print('4.5 元组')

#4.5.1 定义元组【不能给元组的元素赋值】
print('****************')
print('4.5.1 定义元组')

dimensions = (200,50)    #使用圆括号
print(dimensions[0])
print(dimensions[1])

#dimensions = (200,50)   #由于禁止修改元组，当试图修改第一个元素的值，导致返回错误。
#dimensions[0] = 300  

#4.5.2 遍历元组中的所有值
dimensions = (200,50) 
for dimension in dimensions:
    print(dimension)
    
#4.5.3 修改元组的变量
#虽然不能修改元组中的元素，但是可以给存储元组的变量赋值

dimensions = (200,50) 
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)
    
dimensions = (400,100) 
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)    
    
    
    
    





    