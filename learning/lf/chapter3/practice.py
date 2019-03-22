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


#3.2 修改、添加和删除元素
print('****************')
print('3.2 修改、添加和删除元素')

#3-4 嘉宾名单
guests = ['Jack','Alice','Susan']
for m in guests:
    print(m + ", ","would you come to my home to have dinner with me tonight?")

#3-5 修改嘉宾名单
print(guests[1] + " won't come tonight.")

guests[1] = 'Mike'
for m in guests:
    print(m + ", ","would you come to my home to have dinner with me tonight?")

#3-6 添加嘉宾
guests.insert(0, 'Smith')
guests.insert(2, 'Lucy')
guests.append('Amber')
print(guests)

#3-7 缩减名单

print("Only Jack and Susan will come tonight.")

guests.pop(0)
guests.pop(-1)    #注意：删除一个元素之后，列表各元素的索引可能发生变化
guests.pop(1)
guests.pop(1)
print(guests)

del guests[0]
del guests[0]    #注意：这里不能del guests[1]，因为前面一个删除后只剩一个元素，它的新索引是0
print(guests)




