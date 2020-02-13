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
    