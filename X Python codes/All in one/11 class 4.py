class Numbers :
    
    def __init__(self,num) :
        
        self.num=num
        
    def __add__(self,num2):
        print ("let add")
        return self.num + num2.num
        
n1=Numbers(3)
n2=Numbers(6)
sum = n1 + n2
print (sum)
        