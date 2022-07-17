from pyexpat import features
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report
import matplotlib.pyplot as plt
# from mlxtend.plotting import plot_decision_regions

iris = datasets.load_iris()

# print(iris.DESCR)

features = iris.data
label = iris.target

x_train,x_test,y_train,y_test = train_test_split(features,label,test_size=0.33,random_state=42)

clf = KNeighborsClassifier()
clf.fit(x_train,y_train)

predict = clf.predict(x_test)
# print(y_test)

cm= confusion_matrix(y_test,predict)
print(cm)
print(predict)
print("accuracy:",((19+30)/50)*100,'%')
print(classification_report(y_test,predict))

# plot_decision_regions(x, y, clf=clf, legend=2)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Knn with K='+ str(k))
# plt.show()

