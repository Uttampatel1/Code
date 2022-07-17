def furnags(normal,*args,**kwargs):
    print (type(normal))
    print (type(args))
    print (type(kwargs))
    print (normal, "\n")
    for item in args:
        print (item)
        
    print ("\nfor friends data in Programming:\n")
    for key,value in kwargs.items() :
        print (f"{key} is a {value}")
        
        
normal="\nthis is a students are their:" 
    
'''far={"uttam","ayush","harry" ,"hiren", "milan","manthn","dhuli","dhruval","ui"}
kwargs={"utam":"smart boy","ayush": "physical fitness boy","harry":"best teacher"}'''
furnags(normal)
