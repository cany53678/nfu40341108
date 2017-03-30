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

  


```bat

```  


## Table of Contents
4. [Linear Algebra](https://github.com/joelgrus/data-science-from-scratch/blob/master/code/linear_algebra.py)
