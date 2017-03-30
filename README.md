巧欣的筆記
=========================

Homework--0330--numpy
```python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

np.random.seed(sum(map(ord, "aesthetics")))

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

sinplot()
plt.show()
```
Homework--0330--pandas

```python
import pandas as pd
from pandas import Series, DataFrame
data = {"name":["yahoo","google","facebook"], "marks":[200,400,800], "price":[9, 3, 7]}
f1 = DataFrame(data)
print f1
```

Example--0330--pandas


```bat
# coding=UTF-8

import pandas as pd
import numpy as np

num_friends = pd.Series([100,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,
               13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,
               10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,
               8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,
               6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,
               5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,
               4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2
                ,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])

num_newFriends =  pd.Series(np.sort(np.random.binomial(203,0.06,204))[::-1]) #用A series去建立B series
df_friendsGroup = pd.DataFrame({"A":num_friends,"B":num_newFriends}) #將兩張series合成為一個DataFrame

print("印出Col A")
print(df_friendsGroup["A"])
print("印出Col A及Col B的前10row")
select = df_friendsGroup[["A", "B"]]
print(select.head(10))
print("印出row5")
print(df_friendsGroup.ix[5])
print("印出row5~row9")
print(df_friendsGroup[5:10])
```  

## Table of Contents
4. [Linear Algebra](https://github.com/joelgrus/data-science-from-scratch/blob/master/code/linear_algebra.py)
