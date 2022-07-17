class complex:
    
    def __init__(self,r,i) :
        self.real = r
        self.imaginary = i
        
    def __add__(self,c) :
        return complex(self.real+c.real,self.imaginary+c.imaginary)
        
    def __mul__(self,c) :
        mulreal = self.real * c.real - self.imaginary*c.imaginary
        mulimg = self.real*c.imaginary + self.imaginary*c.real
        return complex(mulreal,mulimg)
        
    def __str__(self) :
        if self.imaginary<0 :
            return f"{self.real} - {-self.imaginary}i"
        return f"{self.real} + {self.imaginary}i"
        
n1= complex (3,-7)
n2 = complex (2,-9)
print (n1+n2)
print (n1*n2) 