def remove (string, word) :
    newstr=string.replace(word,"")
    return newstr.strip()
    
this ="          uttam is a good  boy.            "
n=remove(this,"uttam")
print(n)