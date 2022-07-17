def matrix (m,n):
	o = []
	for i in range(m):
		row=[]
		for j in range(n):
			inp = int (input(f"Enter 0[{i+1}][{j+1}] : "))
			row.append(inp)
		o.append(row)
	return o
	
def matrixC (m,n):
	o = []
	for i in range(m):
		row=[]
		for j in range(n):
			row.append(int(0))
		o.append(row)
	return o
	
m1 = int (input("Enter value of m for A matrix: "))
n1 = int (input("Enter value of n for A matrix: "))
print ("\nEnter value of A \n")
A =matrix(m1,n1)
'''A =[[1,2,3],
    [2,3,4],
    [3,4,5]]'''
m2 = int (input("\nEnter value of m for B matrix: "))
n2 = int (input("Enter value of n for B matrix: ")) 
print("\nEnter value of B \n")
B =matrix(m2,n2)
'''B =[[1,0],
    [2,0],
    [3,0]]'''
 
c =matrixC(n1,m2) 
'''c =[[0,0],
    [0,0],
    [0,0]]'''
    
for i in range(len(c)):
	for j in range(len(c[0])):
		for k in range(len(B)):
			c[i][j]+= A[i][k] * B[k][j]
print ("\nThe value of A×B:")
for row in c :
	print(row) 