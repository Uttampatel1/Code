with open ("cryptocurrency.txt") as f:
    lines = f.readlines()
    
currencydict={}
for line in lines:
   # print (line)
    parsed =line.split("\t")
    currencydict[parsed[0]] = parsed[1]
    
amount =int(input("Enter the amount:\n"))
print ("\nenter the name of the currency you want to convert to this amount to ? Available option:\n")
[print(item) for item in currencydict.keys()]
currency =input ("\nplease Enter one of these values:\n")
try :
    print(f"{amount} INR is equal to {amount *float(currencydict[currency])} {currency}")
except :
    print ("please enter right currency")