## -*- coding: utf-8 -*-
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier ##將鄰近的點相連，去模擬出預測值
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

iris = datasets.load_iris() ## 從資料庫裡載入iris的資料
iris_X = iris.data ## iris的屬性，例如花瓣的長寬、花萼的長寬
iris_y = iris.target ## iris的分類

print(iris_X[:2]) ## 顯示前2筆
print(iris_y)
print(np.unique(iris.target)) ## 重複的值不顯示

X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.3)
## 將iris_X和iris_y這2個數據集分成訓練集和測試集，其中測試集佔數據集的30%

print(X_train[:2]) ## 顯示屬性的訓練集(前2筆)
print(X_test[:2]) ## 顯示屬性的測試集(前2筆)
print(y_train) ## 顯示分類的訓練集
print(y_test) ## 顯示分類的測試集

knn = KNeighborsClassifier()
print(knn.get_params()) ## 取出之前定義的參數
knn.fit(X_train, y_train) ## 訓練模型
print(knn.predict(X_test)) ## 預測測試集的數據
print(y_test) ## 真實值

x_min, x_max = iris_X[:, 0].min() - .5, iris_X[:, 0].max() + .5
y_min, y_max = iris_X[:, 1].min() - .5, iris_X[:, 1].max() + .5
plt.figure(2, figsize=(10, 8))

# plt.clf()
# Plot the training points

plt.scatter(iris_X[:, 0], iris_X[:, 1], c=iris_y, cmap=plt.cm.Paired)
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.show()

## 3D圖
fig = plt.figure()
ax = Axes3D(fig, elev=-150, azim=110)
ax.scatter(iris_X[:, 0], iris_X[:, 1], iris_X[:, 2], c=iris_y,
           cmap=plt.cm.Paired)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])

plt.show()