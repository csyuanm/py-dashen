#coding=utf-8

#3.2 修改、添加和删除元素

#3.2.1 修改列表元素
print('****************')
print('3.2.1 修改列表元素')

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'     #修改列表的第一个元素
print(motorcycles)


#3.2.2 在列表中添加元素
print('****************')
print('3.2.2 在列表中添加元素')

#1.在列表末尾添加元素【使用方法append()】
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducati')   #方法append()将元素'ducati'添加列表末尾
print(motorcycles)

#方法append()能够动态创建列表
motorcycles = []     #先创建一个空列表，再使用一系列的append()语句添加元素。
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#2.在列表中插入元素【使用方法insert()】
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')     #使用方法insert()可在列表的任何位置添加新元素
print(motorcycles)


#3.2.3 从列表中删除元素
print('****************')
print('3.2.3 从列表中删除元素')

#1.使用del语句删除元素 【只要知道其索引，便可使用语句del删除列表中的任何一个元素】
#使用del语句将值从列表中删除后，就无法再访问该值。

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[0]   #使用del删除列表中的第一个元素
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[1]   #使用del删除列表中的第二个元素
print(motorcycles)

#2.使用方法pop()删除元素【只要知道其索引，便可使用方法pop()删除列表中的任何一个元素】
#使用该方法可使得删除元素后，能让你接着使用它；被弹出的元素不再在列表中了。

#方法pop()使用一：使用方法pop()将值从列表末尾中删除。

motorcycles = ['honda','yamaha','suzuki']   
print(motorcycles)

motorcycles.pop()   #删除列表末尾元素
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']   #定义并打印列表
print(motorcycles)

poped_motorcycle = motorcycles.pop()   #从该列表末尾中弹出一个值，并存到变量poped_motorcycle中
print(motorcycles)
print(poped_motorcycle)

#方法pop()使用二：删除列表中任何位置处的元素（知道要删除元素的索引）。

motorcycles = ['honda','yamaha','suzuki']
motorcycles.pop(0)
print(motorcycles)   #删除列表中的第一个元素   

motorcycles = ['honda','yamaha','suzuki']
first_owned = motorcycles.pop(0)    #弹出列表中的第一个元素并使用它
print('The first motorcycle I owned was a ' + first_owned.title() + '.')


#3.根据值删除元素【不知道要删除的值的位置，使用方法remove()进行删除】
#使用该方法可使得删除元素后，能让你接着使用它
#方法remove()只删除第一个指定的值

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')     #使用方法remove()删除元素
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']   #定义列表内容
print(motorcycles)

too_expensive = 'ducati'    #将值'ducati'存储在变量too_expensive中
motorcycles.remove(too_expensive)   #使用变量too_expensive来告诉Python将哪个值从列表中删除
print(motorcycles)                  #值'ducati'从列表中删除
print("\nA " + too_expensive.title() + " is too expensive for me.")   #但值'ducati'仍存储在变量too_expensive中









