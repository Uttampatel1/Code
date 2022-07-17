import pickle 
import requests 

url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

response = requests.get(url)
response_txt=response.txt
data=response_txt.splitlines()
red=[[i] for i in data ]
'''
#pikling the python objects 
with open('irisData.pkl','wb') as f :
    pickle.dump(red,f)

# Reading pickle file
with open('irisData.pkl','rb') as f :
    data = pickle.lode(f)
print (data)'''