def fiboIter(n):
	premium = 0
	curnum = 1
	for i in range (1,n):
		prvprvnum = premium 
		premium = curnum 
		curnum = premium + prvprvnum
	return curnum 


def fiboRecur(n):
	if n==0:
		return 0
	elif n==1:
		return 1
	else :
		return fiboRecur(n-1)+fiboRecur (n-2)
	
num = int(input("Enter the number :\n"))
#print (f"The fibonacci series {num} value is {fiboRecur(num)}")
print (f"The fibonacci series {num} value is {fiboIter(num)}")


'''
# print the fibonacci series 
nterms =int(input("Enter the Fibonacci sequence : "))

n1 = 0
n2 = 1
count = 0

if (nterms==1):
	print (f"the Fibonacci sequence upto {nterms} is : {n1}")
	
else:
	while count < nterms:
		print (n1,end=',')
		nth=n1+n2
		n1=n2
		n2 = nth
		count +=1'''