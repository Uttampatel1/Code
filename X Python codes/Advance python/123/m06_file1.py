def get(name):
    print ("good morning, ",name)
print (__name__) 
if __name__ == '__main__' :
    n=input ("Enter the name:\n")
    get(n)
else:
    print ("hiii")