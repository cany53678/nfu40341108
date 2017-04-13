## -*- coding: utf-8 -*-
from sklearn import preprocessing ## 標準化數據模型
import numpy as np
from sklearn.model_selection import train_test_split  ## train與將資料分割與test的模型
from sklearn.datasets.samples_generator import make_classification  ## 生成適合做classification資料的模型
from sklearn.svm import SVC  # Support Vector Machine中的Support Vector Classifier
import matplotlib.pyplot as plt


## 數據標準化的範例
# 建立Array，第一個屬性範圍為-100 ~120；第二個屬性範圍為2.7 ~ 20；第三個屬性範圍為-2 ~ 40
a = np.array([[10, 2.7, 3.6],
              [-100, 5, -2],
              [120, 20, 40]], dtype=np.float64)
# print(a)
# #將normalized後的a印出
# print(preprocessing.scale(a))

## 數據標準化對機器學習成效的影響

# 建立具有2種屬性(n_features=2)的300筆數據(n_samples=300)，其中有2個相關的屬性(n_informative=2)，
# random_state是隨機數的種子，n_clusters_per_class每個分類的集群數
X, y = make_classification(
    n_samples=300, n_features=2,
    n_redundant=0, n_informative=2,
    random_state=22, n_clusters_per_class=1,
    scale=100)

print(X[:5])
print(y)

plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()

# 數據標準化前
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
## 將X和y這2個數據集分成訓練集和測試集，其中測試集佔數據集的30%

clf = SVC()     ## 使用SVC()這個模型
clf.fit(X_train, y_train)         ## 訓練模型
print(clf.score(X_test, y_test))  ## 顯示測試及的精確度


# 數據標準化後
X = preprocessing.scale(X)

plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
## 將X和y這2個數據集分成訓練集和測試集，其中測試集佔數據集的30%

clf = SVC()     ## 使用SVC()這個模型
clf.fit(X_train, y_train)           ## 訓練模型
print(clf.score(X_test, y_test))    ## 顯示測試及的精確度
