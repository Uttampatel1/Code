
def matrix (m,n):
	o = []
	for i in range(m):
		row=[]
		for j in range(n):
			inp = int (input(f"Enter 0[{i+1}][{j+1}] : "))
			row.append(inp)
		o.append(row)
	return o
	
def sum (A,B):
		output = []
		for i in range(len(A)):
			row = []
			for j in range(len(A[0])):
				row.append(A[i][j]+B[i][j])
			output.append(row)
		return output #
#if '__name__'=='__main__' :
	

m = int (input("Enter value of m:\n"))
n = int (input("Enter value of n:\n"))
	
print ("Enter matrix A :")
A = matrix(m,n)
print (f"matrix of A : {A}")

print("Enter matrix B :")
B = matrix(m,n)
print (f"matrix of B : {B}")
 
s = sum(A,B)
print(f"sum of A and B is :{s} ") 