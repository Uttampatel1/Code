import hashlib 
hash_object = hashlib.sha1(b'Hello word')
hex_dig = hash_object.hexdigest()
print (hex_dig)