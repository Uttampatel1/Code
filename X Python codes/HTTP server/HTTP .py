import requests
import os 
from PIL import Image
from IPython.display import IFrame

'''url='https://www.ibm.com/'
r=requests.get(url)

r.status_code
print (r.status_code)

print("request body:", r.request.body)

header=r.headers
print(header)
print(header['date'])
print(header['Content-Type'])

print(r.encoding)

print (r.text[0:100])
# Use single quotation marks for defining string
url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'

r=requests.get(url)
print(r.headers)
r.headers['Content-Type']

path=os.path.join(os.getcwd(),'image.png')
path

with open(path,'wb') as f:
    f.write(r.content)
    
Image.open(path)'''

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt' 

path=os.path.join(os.getcwd(),'example1.txt') 
r=requests.get(url) 
with open(path,'wb') as f:
	f.write(r.content)