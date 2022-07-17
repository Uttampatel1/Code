import random
def gamewin(com,you):
    if (com=='s'):
        if (you=='g'):
            return True 
        elif (you=='w'):
            return False 
    elif (com=='w'):
        if (you=='s'):
            return True 
        elif (you=='g'):
            return False 
    elif (com=='g'):
        if (you=='w'):
            return True 
        elif (you=='s'):
            return False 
    
a=random.randint(1,3)
if (a==1) :
    com='s'
elif (a==2):
    com='w'
else:
    com='g'
print ("computer turn:  Sanke(s),water(w) and gan(g)?")

you =input ("you turn: Sanke(s), water(w) and gan(g)?")
print (f"computer chose: {com}" )
print (f"you chose : {you}")
win=gamewin(com,you)
if (win==None) :
    print ("🤭game is tie!🤠 ")
elif (win==True) :
    print ("🥳🥳you win ! 🥳🥳")
elif (win==False):
    print (" you lose!  try again😜♨️")
