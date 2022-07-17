import numpy as np
'''a = [[1,2,3],[2,3,4], [3,4,5]]
A = np.array(a)
print (A.ndim)
b=A.shape
print (b)
print (A.size)
print (A[1,2])
print (A[1][2])'''
x = np.array ([[1,0,1],[1,1,0]])
y = np.array ([[1,0],[2,3],[7,8]])
z = np.dot(x,y)
print (z)
print (np.sin(z))
w=y.T
print (y)
print (w)