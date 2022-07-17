import time
'''initial=time.time()
k=0
while (k<45):
    print ("this is a uttam bhai")
    k+=1
a=time.time()- initial    
print (f"while loop time is {a} seconds ")
initial2=time.time()
for i in range(45):
    print ("this is a uttam bhai")
b=time.time()- initial2
print (f"for loops time is {b}")

avg=(a+b)/2
print ("the average time is loops",avg)'''

k=0
while k<100000 :
    localtime1=time.asctime(time.localtime(time. time()))
    print (localtime1)
    time.sleep(1)
    k+=1