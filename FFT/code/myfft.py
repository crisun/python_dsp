import numpy as np

def myfft(xn, N):
	if N & (N-1) != 0 or N < len(xn):
		print('Syntax Error!')
		print('Function: myfft(xn, N)')
		print('   Usage: 1.N must be the power of 2')
		print('          2.N must be greater or equal to the length of xn')
		return ;
myfft([1, 2, 3], 3)
