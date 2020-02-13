#单位抽样序列

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5,6)
y = np.zeros(np.size(n))

y[np.where(n==0)] = 1

plt.stem(n,y)
plt.xlabel('n')
plt.xticks(np.arange(-5,6))
plt.ylabel('y')
plt.yticks([0,1])
plt.title(r'$unit\ sample\ seq\ \delta(n)$')

plt.show()