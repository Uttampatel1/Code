def sum(n):
    if (n==1 or n==0) :
        return 1
    else :
      return n + sum(n-1)
    
a=int(input("enter the number of sum : "))

sums=sum(a)
print (sums)
