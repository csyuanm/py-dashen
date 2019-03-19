#使用方法修改字符串的大小写
print('————————')

name='ada lovelace'
print(name.title())   #方法title()以首字母大写的方式显示每个单词

name='Ada Lovelace'
print(name.upper())   #方法upper()将字符串全部改为大写
print(name.lower())   #方法lower()将字符串全部改为小写


#合并（拼接）字符串
print('————————')

first_name='ada'
last_name='lovelace'
full_name='ada'+' '+'lovelace'   #Python用加号（+）来合并字符串
print(full_name)

first_name='ada'
last_name='lovelace'
full_name=first_name+' '+last_name
print('Hello, '+full_name.title()+'!')   #拼接


#使用制表符(\t)或者换行符(\n)来添加空白
print('————————')

print('Python')
print('\tPython')    #添加制表符'\t'
print('Languages:\tPython\thjhjhj3434\tC567\tJavaScript')    #字符串"\t"   ???????????
print('Languages:\tPythn43434\t4hjhjj\tC6734353252\tJavaScrit')    #字符串"\t"  ???????????
print('Languages:\tPyhon\t3hjhj\tC67\tJaScript')    #字符串"\t"

print('--')
print('Languages:\nPython\nC\nJavaScript')    #字符串"\n"让Python换到下一行
print('---')
print('Languages:\n\tPython\n\tC\n\tJavaScript')   #字符串"\n\t"让Python换到下一行，并在下一行开头添加制表符。

print('Languages:\t\nPython\t\nC\t\nJavaScript')   #只能先换行再制表，顺序不能反！！！！！！








