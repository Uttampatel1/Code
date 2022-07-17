n=int (input("what is a apples do you there : "))
mn=int (input("what is minimum number of parts: "))
mx=int(input("what is maximum number of parts: "))

for i in range (mn,mx+1):
	if n%i==0:
		print (f"{i} is divider of {n}")
	else:
		print (f"{i} is not divider of {n}")