num1 = int (input("Enter the fist number \n"))
num2 = int (input("Enter the second number \n"))

if num1>num2 :
	mn=num2
else :
	mn=num1
	
for i in range(1,mn+1):
	if num1%i==0 and num2%i==0 :
		hcf=i 
print (f"The HCF/GCD of these two numbers : {hcf}")