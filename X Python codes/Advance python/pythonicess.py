def sum(A,y,*args,**kwargs):
	print (A)
	print (args)
	print (kwargs)
	
sum(1,2,3,4,5,a=6,b=67,c=87)

a,b,*c,d = [1,2,3,4,5,6,7,8,9,10]
print (a)
print (b)
print (c)
print (d)

status = 1
msg = "Logout" if status==1 else "Login"
print (msg)