list1=[["uttam",2],["ayush",3],["Harry", 6],["hiren",48],["milan",93]]
print (list1)
d=dict(list1)
print (type(d))

for item,lollipop in list1:
    print (item,lollipop)
print (  "\n ******* \n "  )
    
for item, lollipop in d. items():
    print (item, lollipop)