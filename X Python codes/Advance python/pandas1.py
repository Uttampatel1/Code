import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv') 
col = df['Fare']

small_df = df[['Age','Sex','Survived']]
arr = df[['Age','Sex','Survived']].values[:10]

mask = arr[:,2] < 18

#plt.scatter(df['Age'],df['Fare'])
#plt.scatter(df['Age'],c=df['Fare'])
plt.scatter(df['Fare'],df['Age'],c=df['Pclass'])
#plt.plot([0,85],[80,5])
plt.show()
#print (mask)
#print ((arr[:,2]<18).sum())

#print (arr[arr[:,2] < 18])
#print (arr[:,0])
#print (arr[1])
#print (small_df.head())

'''
print (df.head())
print(df.describe())
print(col)'''


'''

import pandas as pd 


df = pd.read_csv('titanic.csv') 

df1 = df['male'] = df['Sex'] == 'male'
#print (df1)

x = df[['Pclass','male','Age','Siblings/Spouses','Parents/Children', 'Fare']].values

y= df['Survived'].values
print (x)
print (y)
'''
