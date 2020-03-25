import math
import numpy as np

def myfft(xn, N = None):
    if N == None:
        N = nextpow2(len(xn))
    if ispow2(N) == False  or N < len(xn):
        print('Parameter Error')
        print('Function: myfft(xn, N)')
        print('Parameters')
        print('xn : array_like')
        print('     Input array, can be complex')
        print(' N : int, optional ')
        print('     The Number of sampling point in frequency domain')
        print('return')
        print('Xk : array_like')
        print('   : Output array, complex')
        print('Tips')
        print('Usage: 1.N must be the power of 2')
        print('       2.N must be greater or equal to the length of xn')
        return 

    #add zero to the end of xn
    xn = np.append(xn, np.zeros(N - len(xn)))
    
    #bit-reverse order input
    Xk = np.array([], dtype = complex)
    for i in range(0, N):
        a = bin2dec(dec2bin(i, N)[::-1])
        Xk = np.append(Xk, xn[a])
    
    #main loop
    levels = int(math.log2(N))          #the num of level

    for level in range(1, levels + 1):
        NumOfGroup = int(N / (2**level))
        GroupInterval = 2**level
        BSInterval = 2**(level - 1)
        Wn = np.exp(-1j * 2 * math.pi / GroupInterval)

        for g in range(NumOfGroup):
            start1 = g * GroupInterval
            start2 = g * GroupInterval + BSInterval

            for b in range(BSInterval):
                Xk[b + start1] = Xk[b + start1] + Xk[b + start2] * (Wn**b)
                Xk[b + start2] = Xk[b + start1] - Xk[b + start2] * (Wn**b) * 2
    return Xk

def myifft(Xk, N = None):
    if N == None :
        N = nextpow2(len(Xk))
    if ispow2(N) == False or N < len(Xk):
        print('Parameter Error')
        print('Function: myifft(Xk, N)')
        print('Parameters')
        print('Xk : array_like')
        print('     Input array, can be complex')
        print(' N : int, optional ')
        print('     The Number of sampling point in frequency domain')
        print('return')
        print('xn : array_like')
        print('   : Output array, complex')
        print('Tips')
        print('Usage: 1.N must be the power of 2')
        print('       2.N must be greater or equal to the length of Xk')
        return
    return  np.conj(myfft(np.conj(Xk), N)) / N

def ispow2(N):
    return (N & (N - 1)) == 0

def nextpow2(N):
    return  2**(math.ceil(np.log2(N)))

def bin2dec(num):
    N = len(num)
    res = 0
    j = 0
    for i in num:
        res = res + int(i) * 2**(N - 1 - j)
        j += 1
    return res

def dec2bin(num, N):
    res = []
    for i in range(int(math.log2(N))):
        num, rem = divmod(num, 2)
        res.append(rem)
    return ''.join([str(x) for x in res[::-1]])

