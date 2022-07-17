def encrypt(plaintext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    plaintext_int = [ord(i) for i in plaintext]
    ciphertext = ''
    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26
        ciphertext += chr(value + 65)
    return ciphertext

def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext
    
String = input ("Enter the string: ")
key = input("Enter the key:")
'''
ch =int(input("1 for encryption and 2 for decryption: "))

if (ch==1):
	en =encrypt(String,key)
	print("encrypt:",en)
elif (ch==2):
	de=decrypt(String,key)
	print("decrypt:",de)
else:
	print ("choose right option. ")
'''	
en =encrypt(String,key)
print("encrypt:",en)
r = en.lower()
print (r)
de=decrypt(r,key)
print("decrypt:",de)