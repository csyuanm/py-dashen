#coding=utf-8


#8.2 传递实参
print('****************')
print('8.2 传递实参')

#8.2.1 位置实参
print('****************')
print('8.2.1 位置实参')

def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet("hamaster", "harry")


#1.调用函数多次
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet("hamaster", "harry")
describe_pet("dog", "willie")  


#2.位置实参的顺序很重要


#8.2.2 关键字实参
print('****************')
print('8.2.2 关键字实参')

#关键字实参是传递给函数的名称——值对
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet(animal_type="hamaster", pet_name="harry")


#8.2.3 默认值
print('****************')
print('8.2.3 默认值')
#编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，将使用指定的实参值，否则将使用形参的默认值
#使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参。

def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('willie')

#如果要描述的动物不是小狗，可使用类似下面的函数调用：
#由于显式地给animal_type提供了实参，因此python将忽略这个形参的默认值
describe_pet(pet_name="harry", animal_type="hamaster")


#8.2.4 等效的函数调用










  
    
    
    