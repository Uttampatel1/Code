print("enter your ages")

age=int(input())

if age>18 and age<100:
    print("you can drive 🚗 ")
elif age==18:
    print("you are come on official")
elif age>7 and  age<18 :
    print("you can't drive 😒 ")
else :
    print("Error")