from sklearn.linear_model import LogisticRegression
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv') 

df1 = df['male'] = df['Sex'] == 'male'
X = df[['Pclass','male','Age','Siblings/Spouses','Parents/Children','Fare']].values
y= df['Survived'].values


model = LogisticRegression()
model.fit(X,y)

#print (model.predict([[3,True, 22.0,1,0,7.5]]))

#print (model.predict(X[:5]))
print (y[:5])

'''
#Score the Model
y_pred = model.predict(X)
print ((y==y_pred).sum())
print ((y==y_pred).sum()/y.shape[0])
print (model.score(X,y))
'''








'''
print (model.coef_, model.intercept_)
plt.scatter(df['Fare'],df['Age'],c=df['Pclass'])
plt.plot(model.coef_,model.intercept_)
plt.show ()'''


#Accuracy, Precision, Recall & F1 Score in Sklearn

y_pred = model.predict(X)
from sklearn.matrix import accuracy_score,Precision_score,recall_score,f1_score

print ("Accuracy :",accuracy_score())
print ("Precision : ",Precision_score)
print ("F1 :",f1_score)