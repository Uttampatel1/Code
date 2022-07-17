from functools import reduce 
# map

def square (num):
    return num * num 
l =[1,2,3,4,5,6,7,8,9]

print (list(map(lambda a:a*a, l)))


# filter 

def greater_than5(num):
    if num >5:
        return True 
        
    else :
        return False 
      
'''        
l2=[1,28,47,82,73,9,223,2,34]
print(list(filter(greater_than5,l2)))
'''
l2=[1,28,47,82,73,9,223,2,34]
print(list(filter(lambda a:a>5,l2)))


# reduce

fuc=lambda a,b:a+b
l3 = [1,2,3,4,5]
print (reduce(lambda a,b:a+b,l3))