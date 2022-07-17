class Calculator:
    def __init__(self,num) :
        self.number=num
        
    def square(self) :
        print (f"The value of {self.number} square is a {self.number**2}")
    def squareroot(self) :
        print (f"The value of {self.number} squareroot is a {self.number**0.5}")
    def cube(self) :
        print (f"The value of {self.number} cube is a {self.number**3}")
    @staticmethod
    def greet():
        print ("Hello there best Calculator in the world")
    
a=int(input ('enter the value:'))
num=Calculator(a)
operator=int(input("Enter 1 for square, 2 for squareroot, 3 for cube \n "))
num.greet()
if (operator==1):
    num.square()
elif (operator==2):
    num.squareroot()
elif (operator==3) :
    num.cube()
else :
    print ("operator error! ")

     