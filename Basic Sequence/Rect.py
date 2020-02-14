#矩形序列

import numpy as np
import matplotlib.pyplot as plt

N = 5
n = np.arange(-5,N+5)
y = np.zeros(np.size(n))
y[np.where((n>=0)&(n<N))] = 1

plt.stem(n,y)
plt.xlabel('n')
plt.xticks(np.arange(-5,N+5))
plt.ylabel('y')
plt.yticks([0,1])
plt.title(f'$R_{N}(n)$')#f-String only for Python3.6+

plt.show()