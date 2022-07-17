
import random 
import string 

if __name__ =='__main__' :
    
    try :
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation
        
        plen = int(input("Enter password length :\n"))
        
        s=[]
        s.extend(s1)
        s.extend(s2)
        s.extend(s3)
        s.extend(s4)
        random.shuffle(s)
        print ("your password is: "+"".join(s[:plen]))
        print("your password is: "+"".join(random.sample(s,plen)))
    except ValueError:
        print ("Oop!, please Enter number!")
        
'''        
import random 
import string 

try:
	s1 = string.ascii_lowercase
	s2 = string.ascii_uppercase
	s3 = string.digits
	s4 = string.punctuation
	plen = int(input("Enter password length :\n"))
	s = str(s1)+str(s2)+str(s3)+str(s4)
	
	password ="".join(random.sample(s,plen))
	print (f'your password is : {password}')
except Exception:
	print ("check the input!")
	'''
    