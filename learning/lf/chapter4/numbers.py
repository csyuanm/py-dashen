#coding=utf-8

#4.3 创建数值列表
print('****************')
print('4.3 创建数值列表')


#4.3.1 使用函数range()
print('****************')
print('4.3.1 使用函数range()')

for value in range(1,5):   #生成1到4的一串数字
    print(value)


#4.3.2 使用函数range()创建数字列表
print('****************')
print('4.3.2 使用函数range()创建数字列表')

numbers = list(range(1,6))   #使用函数list()将range()的结果直接转换为列表
print(numbers)

even_numbers = list(range(2,11,2))  #函数range()从2开始，不断加2，知道达到终值（11）
print(even_numbers)

squares = []                   #先创建一个空列表
for value in range(1,11):      #使用函数range()遍历1-10的值         
    square = value**2          #在循环中，计算当前值的平方，并将结果存储到变量square中
    squares.append(square)     #将新计算的平方值附加到列表squares的末尾
print(squares)

squares = []                   #先创建一个空列表
for value in range(1,11):      #使用函数range()遍历1-10的值         
    squares.append(value**2)     #在循环中，计算当前值的平方，将新计算的平方值附加到列表squares的末尾
print(squares)



#4.3.3 对数字列表执行简单的统计计算
print('****************')
print('4.3.3 对数字列表执行简单的统计计算')

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))   #找出列表最小值
print(max(digits))   #找出列表最大值
print(sum(digits))   #求列表值之和


#4.3.4 列表解析
#列表解析将for循环和创建列表的代码合成一行，并自动附加新元素
print('****************')
print('4.3.4 列表解析')

squares = [value**2 for value in range(1,11)]
print(squares)











