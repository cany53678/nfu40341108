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
Homework--0330--
[pandas](http://wiki.jikexueyuan.com/project/start-learning-python/311.html)

```bat
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

Example--0406--Probability

```bat
def plot_normal_pdfs(plt):
    xs = [x / 10.0 for x in range(-50, 50)]
    plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
    plt.plot(xs, [normal_pdf(x, sigma=0.1) for x in xs], '--', label='mu=0,sigma=0.1')
    plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
    plt.plot(xs, [normal_pdf(x, mu=-1) for x in xs], '-.', label='mu=-1,sigma=1')
    plt.plot(xs, [normal_pdf(x, mu=3, sigma=0.5) for x in xs], '-.', label='mu=3,sigma=0.5')
    plt.plot(xs, [normal_pdf(x, mu=-2) for x in xs], '-.', label='mu=-2,sigma=1')
    plt.legend()
    plt.show()
    
a1=0
    a2=0
    aboth=0
    n=10000
    random.seed(2)
    for _ in range(n):
        get1 = random_ball()
        get2 = random_ball()
        if get1=="B":
            a1 +=1
        if get1=="B" and get2=="B":
            aboth +=1
        if get2=="B":
            a2 +=1

    print "P(both):",aboth/n
    print "P(get1):", a1 / n
    print "P(get2):", a2 / n
    print "P(get1,get2):", a1*a2/n / n
    print "P(get1|get2)=p(both)/p(get2)=",(aboth/n)/(a2/n)
    print "P(get1|get2)=P(get1,get2)/p(get2)=P(get1)p(get2)/p(get2)=P(get1)",  (a1 / n)
```  
Example--0406--Hypothesis and Inference
```
    p=0.99
    a=0.46
    mu_0, sigma_0 = normal_approximation_to_binomial(1000, a)
    print("mu_0", mu_0)
    print("sigma_0", sigma_0)
    print("normal_two_sided_bounds("+str(p)+", mu_0, sigma_0)", normal_two_sided_bounds(p, mu_0, sigma_0))
    print
``` 
## Table of Contents
4. [Linear Algebra](https://github.com/joelgrus/data-science-from-scratch/blob/master/code/linear_algebra.py)
6. [Probability](https://github.com/joelgrus/data-science-from-scratch/blob/master/code/probability.py)
7. [Hypothesis and Inference](https://github.com/joelgrus/data-science-from-scratch/blob/master/code/hypothesis_and_inference.py)