def factorial(number) :
    if number ==0 or number == 1 :
        return 1
    else :
        return number* factorial(number-1)
        
def factorialTrailingZeroe(number) :
     count =0
     i=5
     while (number//i !=0):
         count += int (number/i)
         i *=5
     return count 
     '''   fac = factorial(number)
        count =0
        while (fac%10==0):
            count += 1
            fac /=10
        return count '''
        
        
if __name__ == '__main__' :
    num =int(input("Enter tha number :\n"))
   # print (f"the value of factorial is {factorial(num)}")
    print (f"the value of factorialTrailingZeroe is {factorialTrailingZeroe(num)}") 