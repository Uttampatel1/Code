num=int (input("enter the row : "))
num2=bool(int(input("enter the value of 0 or 1 :  ")))

print (num2)
for i in range(1,num+1):
    if (num2==True):
        print ("*"*i)
    else :
        print ("*"*(num+1-i))