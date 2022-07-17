class Parson :
    country ="India"
    def takebreath(self):
        print ("I am breathing...")
        
class Employee (Parson) :
    company ="Google"
    def takebreath(self) :
        super().takebreath ()
        print ("I am in employee so am lucky breathing....")
        
class Programer (Employee) :
    company ="fiverr"
    def takebreath(self) :
        super().takebreath ()
        print ("I am a programmer so I breathing++....")
        
pe=Parson ()
pe.takebreath ()
e=Employee ()
pr=Programer ()
e.takebreath ()
pr.takebreath ()