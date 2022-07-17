class Numbers :
	def __init__(self,num):
		self.nums = num
		
	def __add__(self,num2):
		print ("lets add")
		return self.nums + num2.nums
	def __sub__(self,num2):
		print ("lets sub")
		return self.nums - num2.nums
	def __str__(self):
		return f"Decimal Numbers :{self.nums}"
		
	def __len__(self):
		return 1		
n1 = Numbers(4)
print (n1)
print (len(n1))
n2 = Numbers(9)
print (n2)
sum =n1+n2
sub = n2-n1
print (sum)
print (sub)