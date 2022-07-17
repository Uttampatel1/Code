from string import digits 
from itertools import product 
import time
a1=time.time()
for passcode in product(digits,repeat=4):
	print ("".join(passcode))
a2=time.time ()
print (a1)
print (a2)
print (a2-a1)