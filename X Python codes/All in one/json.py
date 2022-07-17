import json

# string to dictionary convert 
data='{"name":"utam","language": ["pyhton","c"]}'
print (data)
parsed =json.loads(data)
print (parsed['language'])

# pyton file to javascript file convert
data2={
    "name":"name",
    "car":["BMW","od"],
    "age":18,
    "laptop":None,
    "val":True}
a_json=json.dumps(data2)
print (a_json)
a_json=json.dumps(data2,sort_keys=True)
print (a_json)

# writing with json

person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

with open('person.json', 'w') as f:
    # writing JSON object
    json.dump(person, f)
    

# Serializing json  

json_object = json.dumps(person, indent = 4) 
  
# Writing to sample.json 

with open("sample.json", "w") as outfile:
	outfile.write(json_object)

print(json_object)



#Reading JSON to a File#

# Opening JSON file 
with open('sample.json', 'r') as openfile: 
  
    # Reading from json file 
    json_object = json.load(openfile) 
  
print(json_object) 
print(type(json_object))
