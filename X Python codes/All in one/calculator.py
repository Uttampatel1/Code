while (True) :
    b=int(input("enter the fist number: "))
    c=int(input("enter the second number: "))
    a=input("enter the operator(+,×,÷,-): ")
    if a=='*' and b==45 and c==3:
        print ("555")
    elif a=='+' and b==56 and c==9:
        print ("77")
    elif a=='/' and b==56 and c==6:
        print ("4")
    elif a=='+':
        print (b+c)
    elif a=='-':
        print (b-c)
    elif a=='×':
        print (b*c)
    elif a=='÷':
        print (b/c)
    else :
        print ("Error")
     
    num=input ("again  calculate 'yes' or 'no': ")
    if (num=='yes') :
        continue
    else:
        break
  