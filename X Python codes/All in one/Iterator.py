def gen(n):
	for i in range(n):
		yield i 
		
obj1 = gen(4)
print (next(obj1))
print (next(obj1))
print (next(obj1))
print (next(obj1))



import bisect

number = 335

a=[11,2,6,4,9,29,0]

print (bisect.bisect(a,number))

bisect.insort(a,number)
print (a)