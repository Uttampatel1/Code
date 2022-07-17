from functools import reduce 
l= [1,2,3,4,5,6,7,8,9,10]
print (list(filter(lambda a:a%5==0,l)))

l=[1,28,47,82,73,9,223,2,34]
print(reduce(max,l))
print ("")