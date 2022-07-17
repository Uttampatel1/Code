import re

str='''
Enter the string ex=(uttampipaliya4@gmail.com)
'''

Gmail =re.findall(r"[a-zA-Z0-9_.+%]+@[a-zA-Z0-9._+%]+[.][a-zA-Z0-9]+",str)
print (Gmail)
