#单位阶跃序列

import numpy as np
import matplotlib.pyplot as plt

#sequence number
n = np.arange(-5,6)
#default all zero
y = np.zeros(np.size(n))

#to get y
y[np.where(n>=0)] = 1

#plt config
plt.stem(n,y)
plt.xticks(np.arange(-5,6))
plt.xlabel('n')
plt.yticks([0,1])
plt.ylabel('y')
plt.title(r'$unit\ step\ seq\ u(n)$')

plt.show()
