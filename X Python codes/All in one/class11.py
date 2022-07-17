class Employee :
    company ="Google"
    def showDetails(self) :
        print (f"this is a employee in {self.company}")
         
class Programer(Employee) :
    company ="you tube"
    language ="python"
    def getlanguage(self) :
        print(f"The language is {self.language}")
        
a=Employee()
a.showDetails()
p=Programer()
p.showDetails()
p.getlanguage()