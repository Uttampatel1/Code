from sklearn import linear_model,datasets
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

diabetes = datasets.load_diabetes()
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])
#print(diabetes.keys())

#print(diabetes.DESCR)

#print(diabetes.data)
diabetes_x = diabetes.data
diabetes_x_train = diabetes_x[:-30]
diabetes_x_test = diabetes_x[-30:]

diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()

model.fit(diabetes_x_train,diabetes_y_train)

diabetes_y_pre = model.predict(diabetes_x_test)


print("mean squeard error:",mean_squared_error(diabetes_y_test,diabetes_y_pre))

print("weight:",model.coef_)
print("intercept:",model.intercept_)
'''
plt.scatter(diabetes_x_test,diabetes_y_test)
plt.plot(diabetes_x_test,diabetes_y_pre)
plt.show()
'''







