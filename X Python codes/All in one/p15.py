with open ("has.txt") as f :
    content=f.read()
content = content.replace("donkey", "%$$^%^#")
with open ("has.txt", "w") as f :
    content=f.write (content)