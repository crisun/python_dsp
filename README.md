# python_dsp
## 一、基本序列(Basic Sequence)
1.单位抽样序列 $\delta(n)$
   
$$\delta(n) =\begin{cases} 1& ,\ n=0\\ 0&,\ n\not ={0} \end{cases}$$

```
  ...
  n = np.arange(-5,6)
  y = np.zeros(np.size(n))
  y[np.where(n==0)] = 1
  ...
```

2.单位阶跃序列 $u(n)$
$$u(n) = \begin{cases}1&,\ n \geq0\\0&,\ n<0\end{cases}$$
```
  ...
  n = np.arange(-5,6)
  y = np.zeros(np.size(n))
  y[np.where(n>=0)] = 1
  ...
```

3.正弦序列 $sin(n)$

例如 
$$y(n)=sin(\frac{\pi}{4}n)$$
其中周期
$$\omega=\frac{2\pi}{\frac{\pi}{4}}=8$$
即以8点为一个周期进行循环
```
...
  n = np.arange(-8,9)
  y = np.sin(math.pi/4*n)
...
```
