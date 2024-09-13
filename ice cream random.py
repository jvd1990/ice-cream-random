#Name
import random
name1 = input("What is your Name First person: ")
name2 = input("What is your Name Second person: ")
print("chocolate = 3 $ strawberry = 2 $ blackberry= 3 $ hazelnut=4 $ vanilla= 2 $ saffron=3 $")
#Order person 1
order1 = input(f"What kind of ice cream would you like,{name1}? ")
#Order person 2 (computer)
order2 = random.randint(1,6)

if order2 == 1:
    print(f"{name1} your ice cream is {order1}")
    print(f"{name2} your ice cream is chokolate")
elif order2 == 2:
    print(f"{name1} your ice cream is {order1}")
    print(f"{name2} your ice cream is strawberry")
elif order2 == 3:
    print(f"{name1} your ice cream is {order1}")
    print(f"{name2} your ice cream is blackberry")
elif order2 == 4:
    print(f"{name1} your ice cream is {order1}")
    print(f"{name2} your ice cream is hazelnut")
elif order2 == 5:
    print(f"{name1} your ice cream is {order1}")
    print(f"{name2} your ice cream is vanilla")
elif order2 == 6:
    print(f"{name1} your ice cream is {order1}")
    print(f"{name2} your ice cream is saffron")

