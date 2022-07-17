import random 
while (True): 
    def gamewin(com,you):
        if com=='s':
            if you=='g':
                return True 
            elif you=='w' :
                return False
        elif com=='g':
            if you=='w':
                return True 
            elif you=='s' :
                return False
        elif com=='w':
            if you=='s':
                return True 
            elif you=='g' :
                return False
            
    print ("com turn : Sanke(s)🐍 water(w)💧 and gan(g)⚔🏹?")
    randomNo=random.randint(1,3)
    if randomNo==1:
        com='s'
    elif randomNo==2:
        com ='g'
    elif randomNo==3:
        com='w'

    you=input ("you turn : Sanke(s)🐍,water(w)💧or gan(g)⚔🏹?\n")

    a=gamewin(com,you)

    print (f"computer choose {com} ")
    print (f"you choose. {you}")

    if a==None:
        print ("game is tie 😑!\n\n")
    elif a==True :
        print ("you win 🥳😇🥳!\n\n")
    
    elif a==False :
        print ("you lose 😝🤯!\n\n")
        
    