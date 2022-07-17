# Enter your code here. Read input from STDIN. Print output to STDOUT
from cv2 import split


n= input().split()


# num = int(input())
res = list(map(int, n))

a  =[]
for i in range((res[0])):
    ins = input().split()
    l1 = list(map(int,ins))
    Sum = sum(l1)  
    
    avg = Sum/float(res[1]) 
    a.append(avg)

for i in range(len(a)):
    print(a[i])
        
    