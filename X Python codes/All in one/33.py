'''l=30
print (l)
def num():
    m=70
    global l
    l =l+30
    print (f"the sum of {l} and {m} is :",m+l)
    
num()
print (l)'''

def uttam():
    
    a=45
    def ayush():
        global a
        a=40
    print ('after calling ayush', a )
    ayush()
    print ('before calling ayush',a )
     
uttam()
print (a)
    