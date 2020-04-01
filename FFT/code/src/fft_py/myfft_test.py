import time
import myfft
import myfft_recursive
import numpy as np
import scipy as sp

start1 = time.time()
Y1     = myfft_recursive.fft([1, 1, 1, 1, 0, 0, 0, 0])
end1   = time.time()
Y1     = np.array(Y1)

start2 = time.time()
Y2     = myfft.myfft([1, 1, 1, 1, 0, 0, 0, 0])
end2   = time.time()

start3 = time.time()
Y3     = np.fft.fft([1, 1, 1, 1, 0, 0, 0, 0])
end3   = time.time()

start4 = time.time()
Y4     = sp.fft.fft([1, 1, 1, 1, 0, 0, 0, 0])
end4   = time.time()

print('----------------------------------------------------------------')
print('Recursive')
print(Y1)
print('Duration: ' + str(end1 - start1) + ' s')
print('----------------------------------------------------------------')
print('Myfft')
print(Y2)
print('Duration: ' + str(end2 - start2) + ' s')
print('----------------------------------------------------------------')
print('Numpy.fft.fft')
print(Y3)
print('Duration: ' + str(end3 - start3) + ' s')
print('----------------------------------------------------------------')
print('Scipy.fft.fft')
print(Y4)
print('Duration: ' + str(end4 - start4) + ' s')
print('----------------------------------------------------------------')
