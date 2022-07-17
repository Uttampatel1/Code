def next_palindrome(n):
	n+=1
	while not isPalindrome(n):
		n+=1
	return n
	
def isPalindrome(n):
	return str(n)==str(n)[::-1]
	
#list=[int (input("Enter the value of number : ")) for i in range(int (input("what items should be add : ")))]
list=[37,7,36,7,3,2,4,67,96,13,644]

list1=[next_palindrome(list[i]) for i in range(len(list)) if list[i] > 10]
print (list)
print ()	
print (list1)