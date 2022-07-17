words = ["donkey", "kaddu", "mote","ulu","this"]
with open ("has.txt") as f :
    content=f.read()
print (content)
for word in words :
    
    content=content.replace(word,"$#$^%&$")
    with open ("has.txt","w") as op :
        op.write(content)
        
print (content)
      
        