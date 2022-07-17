
def next_palindrome(n):
	n+=1
	while not isPalindrome(n):
		n+=1
	return n
	
def isPalindrome(n):
	return str(n)==str(n)[::-1]
items =int (input("what items should be add : "))	
list=[int (input("Enter the value of number : ")) for i in range(items)]
print ()
for i in range(items):
	print (f"next palindrome of {list[i]} is {next_palindrome(list[i])}")






'''
items =int (input("what items should be add : "))

for i  in range(items):
	num=int (input("Enter the value of number : "))
	s=str(num)[:]
	while True:
		num+=1
		if str(num)==str(num)[::-1]:
			print (f"next palindrome of {s} is {num}")
			break
'''

	