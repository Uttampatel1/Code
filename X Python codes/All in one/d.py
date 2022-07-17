words = ["donkey", "kaddu", "mote"]

with open("has.txt") as f:
    content = f.read()


for word in words:
    content = content.replace(word, "$%^@$^#")
    with open("has.txt", "w") as f:
        f.write(content)
print (content)