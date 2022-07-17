a=[2,7,9,6,4,3,5,93,49,8]
'''b=[]
for item in a :
    if item%2==0 :
        b.append(item)
print (b)'''
b=[i for i in a if i%2==0]
print (b)