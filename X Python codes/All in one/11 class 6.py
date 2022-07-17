class Employee:
    salary=100000
    incrment=1.6
    
    @property
    def salaryafterincrment(self) :
        return self.salary*self.incrment
        
    @salaryafterincrment.setter
    def salaryafterincrment(self,sai) :
        self.increment=sai/self.salary
       
e=Employee ()
print (e.salaryafterincrment)
    