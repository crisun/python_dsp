from cmath import exp, pi
import time
from myfft import myfft
import numpy as np
import scipy

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd  = fft(x[1::2])
    T = [exp(-2j*pi*k/N)*odd[k] for k in range(N//2)]
    return [even[k] + T[k] for k in range(N//2)] + [even[k] - T[k] for k in range(N//2)]

start1 = time.time()
Y1 = fft([1, 1, 1, 1, 0, 0, 0, 0])
end1   = time.time()
Y1 = np.array(Y1)

start2 = time.time()
Y2     = myfft([1, 1, 1, 1, 0, 0, 0, 0], 8)
end2   = time.time()

start3 = time.time()
Y3     = np.fft.fft([1, 1, 1, 1, 0, 0, 0, 0], 8)
end3   = time.time()

start4 = time.time()
Y4     = scipy.fft.fft([1, 1, 1, 1, 0, 0, 0, 0], 8)
end4   = time.time()

print('--------------------------')
print('Recursive')
print(Y1)
print(end1 - start1)
print('--------------------------')
print('Myfft')
print(Y2)
print(end2 - start2)
print('--------------------------')
print('Numpy.fft.fft')
print(Y3)
print(end3 - start3)
print('--------------------------')
print('Scipy.fft.fft')
print(Y4)
print(end4 - start4)
print('--------------------------')
