#coding=utf-8

#7-8 熟食店
sandwich_orders = ['a', 'b', 'c']
finished_sandwiches = []

for sandwich in sandwich_orders:
    print("I made your " + sandwich + " sandwich.")

while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    
    finished_sandwiches.append(sandwich_order)

for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
    

#7-9 五香烟熏牛肉卖完了
sandwich_orders = ['a', 'b', 'c']
sandwich_orders.insert(0, 'pastrami')
sandwich_orders.insert(2, 'pastrami')
sandwich_orders.insert(-1, 'pastrami')

print(sandwich_orders)

print("The pastrami is sold out.")  

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print(sandwich_orders)

print(finished_sandwiches)


#7-10 梦想的度假胜地

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which place do you think is the best vacation place?")
    
    responses[name] = response






