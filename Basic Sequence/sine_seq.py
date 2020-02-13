#正弦序列

import numpy as np
import matplotlib.pyplot as plt
import math

n = np.arange(-8,9)
y = np.sin(math.pi/4*n)

plt.stem(n,y)
plt.xlabel('n')
plt.xticks(np.arange(-8,9))
plt.ylabel('y')
plt.title(r'$y=sin(n)$')
plt.grid(True)

plt.show()