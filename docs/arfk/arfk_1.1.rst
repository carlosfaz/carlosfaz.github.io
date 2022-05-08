Mathematical Preliminaries
======================================

Infinite Series
-------------------

$\boxed{\textbf{1.1.1}}$

* Prove that if $\lim _{n \rightarrow \infty} n^{p} u_{n}=A<\infty, p>1,$ the series $\sum_{n=1}^{\infty} u_{n}$ converges.
* Prove that if $\lim _{n \rightarrow \infty} n u_{n}=A>0,$ the series diverges. (The test fails for $\left.A=0 .\right)$ These two tests, known as limit tests, are often convenient for establishing the convergence of a series. They may be treated as comparison tests, comparing with
$$
\sum_{n} n^{-q}, \quad 1 \leq q<p
$$

$\boxed{\textbf{Solution}}$ For $(a)$ Let 
$$\lim _{n \rightarrow \infty} n^{p} u_{n}=A<\infty, \quad p>1$$
Define 
$$
u_{n}=\frac{1}{n^{p}}, \quad  p>1
$$
be a series. Let 
$$
\lim _{m \rightarrow \infty} n^{p} u_{n}=A<\infty, \quad p>1
$$
then $\sum_{n=1}^{\infty} u_{n}$ is convergent by limit comparision test as 
$$
\lim _{n \rightarrow \infty} \frac{u_{n}}{u_{n}}=\lim _{n \rightarrow \infty} \frac{u_{n}}{1 / n^{p}}
$$
$$
=\lim _{n \rightarrow \infty} n^{p} u_{n}=A<\infty
$$
If $A\neq 0$ both, the series $\sum_{n=1}^{\infty} u_{n}$ and $\sum_{n=1}^{\infty} u_{n}$ behave alike as 
$$\sum_{n=1}^{\infty} u_{n} = \sum_{n=1}^{\infty} \frac{1}{n^{p}}$$ is convergent series. If $A\neq 0$ then by limit comparision test, if $
\sum_{n=1}^{\infty} u_{n}$ is convergent then $$\sum_{n=1}^{\infty} \frac{1}{n^p}, \quad p>1$$
is convergent by $p-$test. Therefore $\sum_{n=1}^{\infty} u_{n}$ is convergent series. 

$\boxed{\textbf{1.1.2}}$ If $\displaystyle \lim _{n \rightarrow \infty} \frac{b_{n}}{a_{n}}=K,$ a constant with $0<K<\infty,$ show that $\Sigma_{n} b_{n}$ converges or diverges with $\Sigma a_{n}$

Hint. If $\Sigma a_{n}$ converges, rescale $b_{n}$ to $b_{n}^{\prime}=\dfrac{b_{n}}{2 K} .$ If $\Sigma_{n} a_{n}$ diverges, rescale to $b_{n}^{\prime \prime}=\dfrac{2 b_{n}}{K}$

$\boxed{\textbf{Solution}}$ The objective is to prove that the given series converges or diverges with $\sum_{n=1}^{\infty} a_{n}$
It is given that 
$$\lim_{n\rightarrow \infty} \frac{b_{n}}{a_{n}}=K, \quad 0<K<\infty$$
By the definition of limit of a sequence, for any given $\varepsilon>0$ there exists a positive integer $N$ such that for all 
$$n \geq N,\left|\frac{b_{n}}{a_{n}}-K\right|<\varepsilon$$
This implies, 
$$-\varepsilon<\frac{b_{n}}{a_{n}}-K<\varepsilon$$ for all values of $n \geq N$.
From this the inequality implies, 
$$K-\varepsilon<\frac{b_{n}}{a_{n}}<K+\varepsilon$$
for all $n \geq N$. From the above inequality, 
$$(K-\varepsilon) a_{n}<b_{n}<(K+\varepsilon) a_{n}$$ 
for all $n \geq N$. So, $(K-\varepsilon) a_{n}<b_{n}$ and $b_{n}<(K+\varepsilon) a_{n}$ for all $n \geq N$. Suppose that $\sum_{n=1}^{\infty} a_{n}$ converges. Then, 
$$\sum_{n=1}^{\infty}(K+\varepsilon) a_{n}$$ 
also converges. By the equation above, $b_{n}<(K+\varepsilon) a_{n}$ for all $n \geq N$
By comparison test the series $\sum_{n=1}^{\infty} b_{n}$ also converges. Suppose that $\sum_{n=1}^{\infty} a_{n}$ diverges. Then 
$$\sum_{n=1}^{\infty}(K-\varepsilon) a_{n}$$ 
also diverges. By the above equation 
$$(K-\varepsilon) a_{n}<b_{n}$$
for all $n \geq N$. By the condition $(K-\varepsilon) a_{n}<b_{n}$ for all $n \geq N$. Hence, by comparison test the series $\sum_{n=1}^{\infty} b_{n}$ also diverges.

$\boxed{\textbf{1.1.3}}$

* Show that the series 
$$\sum_{n=2}^{\infty} \frac{1}{n(\ln n)^{2}}$$
converges.
* By direct addition $$\sum_{n=2}^{100,000}\left[n(\ln n)^{2}\right]^{-1}=2.02288$$ Use Eq. (1.9) to make a fivesignificant-figure estimate of the sum of this series.	
$$
\int_{N+1}^{\infty} f(x) d x \leq \sum_{n=N+1}^{\infty} a_{n} \leq \int_{N+1}^{\infty} f(x) d x+a_{N+1} \quad (1.9)
$$

$\boxed{\textbf{Solution}}$ For $(a)$ we check the convergence it is required to use the integral test. Put 
$$f(x)=\frac{1}{x(\ln x)^{2}} \Rightarrow f(n)=\frac{1}{n(\ln n)^{2}}$$
Then, $f(x)$ is a continuous function and monotonically decreasing.
To apply the test, the integral 
$$\int_{2}^{\infty} f(x) d x=\int_{2}^{\infty} \frac{1}{x(\ln x)^{2}} d x$$ 
should be evaluated. Let $\ln x=t \Rightarrow \dfrac{1}{x} d x=d t$
$$
\begin{aligned}
\int f(x) d x &=\int \frac{1}{t^{2}} d t \\
&=\frac{-1}{t} \\
&=\frac{-1}{\ln x}
\end{aligned}
$$
$$
\begin{aligned}
\int_{2}^{\infty} f(x) d x &=\left[\frac{-1}{\ln x}\right]_{2}^{\infty} \\
&=0-\left(\frac{-1}{\ln 2}\right) \\
&=\frac{1}{\ln 2}
\end{aligned}
$$
Therefore the integral of the function is a finite number.
By integral test, $\sum_{n=2}^{\infty} f(n)$ is convergent if the integral is a finite number.
since, the integral is a finite number, 
$$\sum_{n=2}^{\infty} \frac{1}{n(\ln n)^{2}}$$ converges by integral test.

$\boxed{\textbf{Solution}}$ For $(b)$ by addition, it is given that 
$$\sum_{n=2}^{1,00,000}\left[n(\ln n)^{2}\right]^{-1}=2 \cdot 02288$$
It is required to find the sum of the series, 
$$\sum_{n=2}^{\infty}\left[n(\ln n)^{2}\right]^{-1}$$
But, 
$$\sum_{n=2}^{\infty}\left[n(\ln n)^{2}\right]^{-1}=\sum_{n=2}^{N}\left[n(\ln n)^{2}\right]^{-1}+\sum_{n=N+1}^{\infty}\left[n(\ln n)^{2}\right]^{-1}$$
By the inequality, 
$$\int_{N+1}^{\infty} f(x) d x \leq \sum_{n=N+1}^{\infty} a_{n} \leq \int_{N+1}^{\infty} f(x) d x+a_{N+1}$$ 
where 
$$a_{n}=f(n)=\frac{1}{n(\ln n)^{2}}$$
$$
\int_{N+1}^{\infty} \frac{1}{x(\ln x)^{2}} d x \leq \sum_{n=N+1}^{\infty} \frac{1}{n(\ln n)^{2}} \leq \int_{N+1}^{\infty} \frac{1}{x(\ln x)^{2}} d x+a_{N+1}
$$
Put, the value $N=1,00,000$ in the inequality.
$$
\int_{1,00,001}^{\infty} \frac{1}{x(\ln x)^{2}} d x \leq \sum_{n=1,00,001}^{\infty} \frac{1}{n(\ln n)^{2}} \leq \int_{1,00,001}^{\infty} \frac{1}{x(\ln x)^{2}} d x+\frac{1}{1,00,001 \times(\ln 1,00,001)}
$$
$$
\left[\frac{-1}{\ln x}\right]_{1,00,001}^{\infty} \leq \sum_{n=1,00,001}^{\infty} \frac{1}{n(\ln n)^{2}} \leq\left[\frac{-1}{\ln x}\right]_{1,00,001}^{\infty}+\frac{1}{1,00,001 \times(\ln 1,00,001)^{2}}
$$
$$
\frac{1}{\ln 1,00,001} \leq \sum_{n=1,00,001}^{\infty} \frac{1}{n(\ln n)^{2}} \leq \frac{1}{\ln 1,00,001}+0 \cdot 0868500
$$
$$
0.0868588 \leq \sum_{n=1,00,001}^{\infty} \frac{1}{n(\ln n)^{2}} \leq 0 \cdot 0868588+0 \cdot 0868500
$$
$$
0.0868588\leq \sum_{n=1,00,001}^{\infty} \frac{1}{n(\ln n)^{2}} \leq 0 \cdot 0868588754
$$
From the above the value of the sum is 
$$\sum_{n=1,00,001}^{\infty} \frac{1}{n(\ln n)^{2}}=0 \cdot 08686$$
Now, the required value of the sum of the series is
$$
\begin{aligned}
\sum_{n=2}^{\infty}\left[n(\ln n)^{2}\right]^{-1} &=\sum_{n=2}^{1,00,000}\left[n(\ln n)^{2}\right]^{-1}+\sum_{n=1,00,001}^{\infty}\left[n(\ln n)^{2}\right]^{-1} \\
&=2 \cdot 02288+0 \cdot 08686 \\
&=2 \cdot 10974
\end{aligned}
$$
Hence, the required sum is 
$$\sum_{n=2}^{\infty}\left[n(\ln n)^{2}\right]^{-1}=2 \cdot 10974$$




