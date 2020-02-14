# DSP using Python

## 一、基本序列(Basic Sequence)

1.单位抽样序列 
$$
\delta(n) = \begin{cases} 1& ,\ n=0\\ 0&,\ n\not ={0} \end{cases}
$$

##### python代码块

````python
n = np.arange(-5,6)
y = np.zeros(np.size(n))
y[np.where(n==0)] = 1
````

2.单位阶跃序列 
$$
u(n) = \begin{cases}1&,\ n \geq0\\0&,\ n<0\end{cases}
$$

##### python代码块

#####  

```python
n = np.arange(-5,6)
y = np.zeros(np.size(n))
y[np.where(n>=0)] = 1
```

3.正弦序列 

例如 
$$
y(n)=sin(\frac{\pi}{4}n)
$$
其中
$$
\omega=\frac{2\pi}{\frac{\pi}{4}}=8
$$
即以8点为一个周期

```python
n = np.arange(-8,9)
y = np.sin(math.pi/4*n)
```

4.矩形序列
$$
R_N(n) = \begin{cases}1&,\ 0\leq n\leq N-1 \\0& ,\ others\end{cases}
$$
python代码块

```python
N = 5
n = np.arange(-5,N+5)
y = np.zeros(np.size(n))
y[np.where((n>=0)&(n<N))] = 1
```

