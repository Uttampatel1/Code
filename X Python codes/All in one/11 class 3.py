class Employee :
    country ="India"
    salary = 400
    location ="Gujarat"
    
   # def changesalary(self,sal):
      #  self.__class__.salary=sal
        
    @classmethod
    def changesalary(cls,sal) :
        cls.salary=sal
    
    
e=Employee ()
print (e.salary)
e.changesalary(500)
print (e.salary)
print (Employee.salary)
