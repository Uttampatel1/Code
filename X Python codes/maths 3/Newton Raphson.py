def NewtonRhn(x):
	for i in range (8):
#	print (f"x{i}: {x0}")
		f_x1=x**3 - 5*x +3
		f_x2=(3*(x**2))-5
		sm= x - (f_x1/f_x2)
		sm1="{:.4f}".format(sm)
		print (f"x{i+1} = {sm1}")
		x=float(sm1)
	return x
		
print ("f(x) = x^3 - 5x + 3\n")
l1=[0,0.5,1,1.5,2,2.5]

for x in l1:
	f_x = x**3 - 5*x +3
	print (f"f({x}) : {f_x}")

x0=float(input("\nEnter the value of x0 : "))
print ("\nThe real root of equation correct up to 4 decimal places is : ",NewtonRhn(x0))


