for at in range(1,10) :
    a=int(input("choose the number :\n"))
    if (a==78):
        print ("\ncongrats you win !🥳💥\n")
    elif (a<78):
        print ("\nplease enter geater number!\n")
    else :
        print ('\nplease enter lower number!\n')
    if (a==78):
        print ("number of gasses", at)
        break
    print ("number of gasses left!",9-at)
    print ('  \n ')
    if(at==9) :
        print ("game over! 😂")
     
    
        
    