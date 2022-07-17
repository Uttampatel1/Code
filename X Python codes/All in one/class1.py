class Programer:
    company="Google"
    
    
    def __init__(self,name,product) :
        self.name=name
        self.product=product
    
    
    def getInfo(self):
        print (f"the company is {self.company} and name of the programer is {self.name} and the product is {self.product}")

Harry=Programer("Harry","skype")
uttam=Programer("uttam","AI applications")
Harry.getInfo()
uttam.getInfo()     
    
    