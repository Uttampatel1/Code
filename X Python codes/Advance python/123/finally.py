try :
    i=int(input("Enter the number: "))
    n=1/i
    print (n)
    
except Exception as r:
    print (r)
    exit()
    
finally :
    
    print ("thank you")
print ("we are done")