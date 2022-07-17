from cProfile import label
from re import X
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

iris = load_iris()

# print(iris.keys())
# ['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module']

# print(iris.DESCR)

X = iris['data'][:,3:]
# print(X)
y = (iris['target']==2).astype(np.int)
print(y)
x_train,x_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=0)

clf = LogisticRegression()
clf.fit(x_train,y_train)

x_new = np.linspace(0,3,1000).reshape(-1,1)
y_prob = clf.predict_proba(x_new)

plt.plot(x_new,y_prob[:,1],'g-',label="virginica")
plt.show()