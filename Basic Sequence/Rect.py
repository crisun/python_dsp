#矩形序列

import numpy as np
import matplotlib.pyplot as plt

n0 = 5
n = np.arange(-5,n0+5)
y = np.zeros(np.size(n))
y[np.where((n>=0)&(n<n0))] = 1

plt.stem(n,y)
plt.xlabel('n')
plt.xticks(np.arange(-5,n0+5))
plt.ylabel('y')
plt.yticks([0,1])
plt.title(f'$R_{n0}(n)$')#f-String only for Python3.6+

plt.show()