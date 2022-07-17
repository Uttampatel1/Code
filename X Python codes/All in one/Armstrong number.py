n = int (input("Enter the number: \n"))
order = len(str(n))
sum = 0
copy_n = n 
while (n>0) :
    digit = n%10
    sum += digit**order 
    n=n//10
if (sum == copy_n):
    print(f"{copy_n} is an Armstrong number") 
else :
    print(f"{copy_n} is not an Armstrong number") 