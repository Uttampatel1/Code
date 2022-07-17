import requests
import os 
from PIL import Image
from IPython.display import IFrame

#Get Request with URL Parameters

url_get='http://httpbin.org/get'

payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)

print(r.url)

print("request body:", r.request.body)

print(r.status_code)
print(r.text)
print(r.headers['Content-Type'])

print(r.json())

print(r.json()['args'])


##Post Requests

url_post='http://httpbin.org/post'

r_post=requests.post(url_post,data=payload)

print("POST request URL:",r_post.url )
print("GET request URL:",r.url)

print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

print(r_post.json()['form'])