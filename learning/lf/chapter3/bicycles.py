#coding=utf-8

bycicles = ['trek','cannondale','redline','specialized']
print(bycicles)

#访问列表元素
print('****************')
print('访问列表元素')

bycicles = ['trek','cannondale','redline','specialized']
print(bycicles[0])   #第一个列表元素的索引为0，而不是1
print(bycicles[0].title())

print(bycicles[1])   #返回列表第2个元素
print(bycicles[3])   #返回列表第4个元素

print(bycicles[-1])  #索引-1返回列表最后一个元素；索引-2返回列表倒数第二个元素，以此类推。


#使用列表中的各个值
print('****************')
print('使用列表中的各个值')

bycicles = ['trek','cannondale','redline','specialized']
message = "My first bycicle was a  " + bycicles[0].title() + "."
print(message)






