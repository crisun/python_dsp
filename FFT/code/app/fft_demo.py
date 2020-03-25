import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt

fs = 1024
f1 = 50
f2 = 120
f3 = 480

x = np.linspace(0,1,fs)
y = 6.3*np.sin(2*np.pi*f1*x)+2.8*np.sin(2*np.pi*f2*x)+5.6*np.sin(2*np.pi*f3*x)

Y = fft(y,1024)
Y1 = 2*Y/len(Y)
Y2 = abs(Y1[0:int(len(Y1)/2)])
n = np.arange(fs/2)
plt.plot(n,Y2)
plt.xticks(np.arange(0,fs/2,20))
plt.grid(True)
plt.show()
