from sklearn.linear_model import LogisticRegression
import pandas as pd 
from sklearn.model_selection import train_test_split
#from sklearn.matrix import accuracy_score,Precision_score,recall_score,f1_score

df = pd.read_csv('titanic.csv') 

df1 = df['male'] = df['Sex'] == 'male'
X = df[['Pclass','male','Age','Siblings/Spouses','Parents/Children','Fare']].values
y= df['Survived'].values

X_train,X_test,y_train,y_test = train_test_split(X,y)
model = LogisticRegression()
model.fit(X_train,y_train)

"""
print("whole datasets :",X.shape,y.shape)
print ("training set: ",X_train.shape,y_train.shape)
print ("test set  : ",X_test.shape,y_test.shape)
"""

print (model.score(X_test,y_test))

y_pred = model.predict(X_test)

'''
print ("Accuracy :",accuracy_score(y_test,y_pred ))
print ("Precision : ",Precision_score(y_test,y_pred ))
print ("recall :",recall_score(y_test,y_pred))
print ("F1 :",f1_score(y_test,y_pred))
'''
