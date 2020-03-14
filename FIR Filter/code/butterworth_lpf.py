import numpy as np
import matplotlib.pyplot as plt

n = np.linspace(-5,5)
y = n**2
plt.stem(n,y)
plt.savefig('../fig/butterworth_lpf')
