marks1=int(input("enter your mark for maths :\n"))
marks2=int(input("enter your mark for science :\n"))
marks3=int(input("enter your mark for social science :\n"))
marks4=int(input("enter your mark for English:\n"))
marks5=int(input("enter your mark for sanskrut:\n"))
marks6=int(input("enter your mark for gujarati:\n"))
total =marks1+marks2+marks3+marks4+marks5+marks6
print ("total:",total)
t=(total*100)/480
print ("avg:",t)
if (t<=100 and t>90):
    print ("your grade is A+")
elif (t<=90 and t>80) :
    print ("your grade is A")
elif (t<=80 and t>70) :
    print ("your grade is B")
elif (t<=70 and t>60):
    print ("your grade is C")
elif (t<=60 and t>50) :
    print ("your grade is D")
else  :
    print ("your grade is E")

if (marks1>27 and marks2>27 and marks3>27 and marks4>27 and marks5>27 and marks6>27 or t>33.75):
    print ("🥳you are pass 🥳")
else :
    print ("try next time")