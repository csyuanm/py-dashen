
#str()使用避免类型错误

#发生类型错误，Python无法识别你使用的信息。Python发现你使用了一个值可能为整数(int)的变量，但不知道如何解读。
#这个变量可能是数值23，也可能是字符2和3.
#在字符串中使用整数时，需要指出你希望将该整数用作字符串。方法str()能将非字符串表示为字符串。


age = 23
message = "Happy" + str(age) + "rd Birthday"   
print(message) 