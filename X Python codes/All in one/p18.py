content =True 
i=1
with open ("log.txt") as f:
    while content :
            content =f.readline()
            if "python" in content.lower():
                print (content)
                print (f"python is a present in number of line {i}")
            i+=1
            