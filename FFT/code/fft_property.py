import numpy as np
import matplotlib.pyplot as plt

n = np.ones(4)
y1 = abs(np.fft.fft(n).real)
y2 = abs(np.fft.fft(n,8).real)
y3 = abs(np.fft.fft(n,16).real)
y4 = abs(np.fft.fft(n,32).real)

plt.subplot(221)
plt.stem(y1)
plt.title('4-pt FFT')
plt.subplot(222)
plt.stem(y2)
plt.title('8-pt FFT')
plt.subplot(223)
plt.stem(y3)
plt.title('16-pt FFT')
plt.subplot(224)
plt.stem(y4)
plt.title('32-pt FFT')

plt.show()
