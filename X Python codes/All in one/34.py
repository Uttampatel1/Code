def function_fibonacci(n):
    n=n-1
    if (n==0):
        return 0
    elif (n==1) :
        return 1
    else:
        return function_fibonacci(n-1)+function_fibonacci(n-2)
        
        
num =int (input("enter the number for factorial:  "))
a=function_fibonacci(num)

print ("the value of fibonacci :",a)


#0 1 1 2 3 5 8 13