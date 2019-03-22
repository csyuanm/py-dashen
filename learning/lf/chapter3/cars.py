#coding=utf-8

#3.3 组织列表

#3.3.1 使用方法sort()对列表进行永久性排序
print('****************')
print('3.3.1 使用方法sort()对列表进行永久性排序')

cars = ['bmw','audi','toyota','subaru']
cars.sort()     #列表中的元素按照字母顺序排列，使用方法sort()后该排列顺序是永久性的
print(cars)

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)   #向方法sort()传递参数reverse=True，便可按照相反顺序排列列表元素；对列表元素排列顺序的修改也是永久性的。
print(cars)


#3.3.2 使用函数sorted()对列表进行临时排序
print('****************')
print('3.3.2 使用函数sorted()对列表进行临时排序')

#要保留列表元素原来的排列顺序，同时以特定的顺序呈现他们，可使用函数sorted()。
#函数sorted()让你能够安装特定顺序显示列表元素，同时不影响他们在列表中的原始排列顺序。

cars = ['bmw','audi','toyota','subaru']
print(cars)

print("Here is the original list:")
print(cars)             #先按原始顺序打印列表

print("Here is the sorted list:")
print(sorted(cars))     #再按特定书顺序显示列表

print("\nHere is the original list again:")
print(cars)             #列表元素的排列顺序与以前相同

ss = sorted(cars)
print(ss)


