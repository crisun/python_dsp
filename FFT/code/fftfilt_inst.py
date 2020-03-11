import numpy as np
import matplotlib.pyplot as plt

Lx = 41
N = 5
M = 10

hn = np.ones(N)
hn1 = np.array(hn) + np.zeros(Lx - N)
print(hn1)