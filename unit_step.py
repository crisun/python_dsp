#单位阶跃序列

import numpy as np
import matplotlib.pyplot as plt

#sequence number
n = np.arange(-5,5)
#default all zero
y = np.zeros(np.size(n))

#to get y
y[np.where(n>=0)] = 1

#plt config
plt.stem(n,y)
plt.xticks(np.arange(-5,5))
plt.xlabel('n')
plt.ylabel('y')
plt.title('unit_step seq')

plt.show()
