with open ("log.txt") as f:
    content=f.read()
    
if "game is" in content:
    print ("python is a present")
else:
    print ("python is not present")