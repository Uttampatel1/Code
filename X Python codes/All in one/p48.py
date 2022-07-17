'''num=[2,3,4,5,67,28,90]
print (map(int,num))
#num=list(map(int,num))

#for i in range(len(num)):
#    num[i]=int(num[i])
num[2]=num[2]+2
print (num[2])
print (len(num))
number=[2,3,36,7,4,8,8,96,555757,6,5]
square=list(map(lambda a: a*a,number))
print (square)


**************map********

def square(a):
    return a*a
    
def cube(a):
    return a*a*a
    
func=[square,cube]
for i in range(1,6):
    val=list(map(lambda x:x(i),func))
    print (val)
    
#print (val)

*********filter**************functions  = [1,2,3,4,5,6,7,8,9,10]
def if_greater_5(num) :
    return num>5
if_greater_5=list(filter(if_greater_5,list1))
print (if_greater_5)

********reduce************
from functools import reduce

list1 =[1,2,3,4,5,6]
num=0
for i in list1:
    num = num + i
   # print (num)
print (num)
num=reduce(lambda x,y:x*y,list1)
print (num)'''



