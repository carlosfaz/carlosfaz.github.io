Gamma Function
======================================

Properties of Gamma Function
-------------------

$\boxed{\textbf{13.1.1}}$ Derive the recurrence relations
$$
\Gamma(z+1)=z \Gamma(z)
$$
from the Euler integral, Eq. (13.5),
$$
\Gamma(z)=\int_{0}^{\infty} e^{-t} t^{z-1} d t, \quad \Re e(z)>0, \quad \text{Eq.}(13.5)
$$
$\boxed{\textbf{Solution}}$ Consider the Euler integral 
$$\Gamma (z)=\int_{0}^{\infty} e^{-t} t^{z-1} d t$$
Put, $z=z+1$
$$
\begin{aligned}
\Gamma(z+1) &=\int_{0}^{\infty} e^{-t} t^{z+1-1} d t \\
&=\int_{0}^{\infty} e^{-t} t^{z} d t \\
&=t^{z} \int_{0}^{\infty} e^{-t} d t-\int_{0}^{\infty} \frac{d t^{z}}{d x} \int e^{-t} d t \\
=&-t^{z} e^{-t}\Big|_{0} ^{\infty}+z \int_{0}^{\infty} e^{-t} t^{z-1} d t \\
=& z \Gamma(z)
\end{aligned}
$$


$\boxed{\textbf{13.1.2}}$ In a power-series solution for the Legendre functions of the second kind we encounter the expression
$$
\frac{(n+1)(n+2)(n+3) \cdots(n+2 s-1)(n+2 s)}{2 \cdot 4 \cdot 6 \cdot 8 \cdots(2 s-2)(2 s) \cdot(2 n+3)(2 n+5)(2 n+7) \cdots(2 n+2 s+1)}
$$
in which $s$ is a positive integer.
* Rewrite this expression in terms of factorials.
* Rewrite this expression using Pochhammer symbols; see Eq. (1.72).
$$
(a)_{0}=1, \quad(a)_{1}=a,(a)_{n+1}=a(a+1) \cdots(a+n),(n \geq 1), \quad \text{Eq.}(1.72)
$$

$\boxed{\textbf{Solution}}$ For $(a)$ Notice that
$$\frac{(n+1)(n+2)(n+3) \cdots(n+2 s-1)(n+2 s)}{2.4 .6 .8  \cdots (2 s-2)(2 s) \cdot(2 n+3)(2 n+5)(2 n+7) \cdots(2 n+2 s+1)}$$
$$
\begin{aligned}
=&\frac{[n! \ (n+1)(n+2)(n+3) \cdots(n+2 s-1)(n+2 s)]}{n! \  s! \  2^{s} \cdot(2 n+3)(2 n+5)(2 n+7) \cdots(2 n+2 s+1)}\\
&=\frac{(n+2 s) !(2 n+1) !}{n! \  s! \  2^{s} \cdot[(2 n+1) !(2 n+3)(2 n+5)(2 n+7) \cdots(2 n+2 s+1)} \\
&=\frac{(n+2 s) !(2 n+1) ![(2 n+2)(2 n+4)(2 n+6) \cdots(2 n+2 s)]}{n! \  s! \  2^{s} \cdot[(2 n+1) !(2 n+3)(2 n+4)(2 n+5)(2 n+6)(2 n+7) \cdots(2 n+2 s)(2 n+2 s+1)]} \\
& =\frac{(n+2 s) !(2 n+1) ! 2^{s}[(n+1)(n+2)(n+3) \cdots(n+s)]}{n! \  s! \  2^{s} \cdot[(2 n+1) !(2 n+3)(2 n+4)(2 n+5)(2 n+6)(2 n+7) \cdots(2 n+2 s)(2 n+2 s+1)]}\\
&=\frac{(n+2 s) !(2 n+1) ![n! \ (n+1)(n+2)(n+3) \cdots(n+s)]}{n! \  s! \  n! \ [(2 n+1) !(2 n+3)(2 n+4)(2 n+5)(2 n+6)(2 n+7) \cdots(2 n+2 s)(2 n+2 s+1)]} \\
&=\frac{(n+2 s) !(2 n+1) !(n+s) !}{n! \  n! \  s! \ (2 n+2 s+1) !}
\end{aligned}
$$
$\boxed{\textbf{Solution}}$ For $(b)$ we notice that

$$
\frac{(n+1)(n+2)(n+3) \cdots(n+2 s-1)(n+2 s)}{2\cdot 4 \cdot 6 \cdot 8  \cdots (2 s-2)(2 s) \cdot(2 n+3)(2 n+5)(2 n+7) \cdots(2 n+2 s+1)}
$$

$$
\begin{aligned}
&=\frac{(n+1)(n+2)(n+3) \cdots[(n+1)+(2 s-2)][(n+1)+(2 s-1)]}{\left(2^{s}[1 \cdot 2 \cdot 3  \cdots  \cdot(s-1) s]\right) \cdot[(2 n+3)(2 n+5)(2 n+7) \cdots(2 n+2 s+1)]} \\
& =\frac{(n+1)_{(2 s-1)+1} \cdot[(2 n+2)(2 n+4)(2 n+6) \cdots(2 n+2 s)]}{\left(2^{s}[1 \cdot 2 \cdot 3  \cdots  \cdot\{1+(s-2)\}\{1+(s-1)\}) \cdot[(2 n+2)(2 n+3)(2 n+4)(2 n+5) \cdots(2 n+2 s)(2 n+2 s+1)]\right.}\\
&=\frac{(n+1)_{2 s} \cdot[(n+1)(n+2)(n+3) \cdots(n+s)] \cdot 2^{s}}{2^{s}(1)_{(s-1)+1} \cdot[(2 n+2)(2 n+3)(2 n+4) \cdots\{(2 n+2)+(2 s-1)\}]} \\
& =\frac{(n+1)_{2 s} \cdot[(n+1)(n+2)(n+3) \cdots\{(n+1)+(s-1)\}]}{(1)_{s} \cdot(2 n+2)_{(2 s-1)+1}}\\
& =\frac{(n+1)_{2 s} \cdot(n+1)_{(s-1)+1}}{(1)_{s} \cdot(2 n+2)_{2 s}}\\
&=\frac{(n+1)_{2 s} \cdot(n+1)_{s}}{(1)_{s} \cdot(2 n+2)_{2 s}}
\end{aligned}
$$



$\boxed{\textbf{13.1.3}}$ Show that $\Gamma(z)$ may be written
$$\Gamma(z)=2 \int_{0}^{\infty} e^{-t^{2}} t^{2 z-1} d t, \quad \operatorname{Re}(z)>0$$
$$\Gamma(z)=\int_{0}^{1}\left[\ln \left(\frac{1}{t}\right)\right]^{z-1} d t, \quad \Re e(z)>0$$

$\boxed{\textbf{Solution}}$ Changing variables $t=u^{2}$ and $d t=2 u d u$ we have
$$
\begin{aligned}
\Gamma (z) &=\int_{0}^{\infty} e^{-u^{2}} u^{2 z-2} u d u \\
&=\int_{0}^{\infty} e^{-u^{2}} u^{2 z-1} d u \\
&=\int_{0}^{\infty} e^{-t^{2}} t^{2 z-1} d t
\end{aligned}
$$
as $t \rightarrow 0$ to $\infty u \rightarrow 0$ to 1 the equation takes the form of 
$$
\begin{aligned}
\Gamma (z) &=\int_{0}^{1} e^{-\ln \frac{1}{u}}\left(\ln \frac{1}{u}\right)^{z-1} u d u \\
&=\int_{0}^{1} u\left(\ln \frac{1}{u}\right)^{z-1} u d u \\
&=\int_{0}^{1}\left(\ln \frac{1}{u}\right)^{z-1} d u \\
&=\int_{0}^{1}\left(\ln \frac{1}{t}\right)^{z-1} d t
\end{aligned}
$$


$\boxed{\textbf{13.1.4}}$ In a Maxwellian distribution the fraction of particles of mass $m$ with speed between $v$ and $v+d v$ is
$$
\frac{d N}{N}=4 \pi\left(\frac{m}{2 \pi k T}\right)^{3 / 2} \exp \left(-\frac{m v^{2}}{2 k T}\right) v^{2} d v
$$
where $N$ is the total number of particles, $k$ is Boltzmann's constant, and $T$ is the absolute temperature. The average or expectation value of $v^{n}$ is defined as $\left\langle v^{n}\right\rangle=$ $N^{-1} \int v^{n} d N .$ Show that
$$
\left\langle v^{n}\right\rangle=\left(\frac{2 k T}{m}\right)^{n / 2} \frac{\Gamma\left(\frac{n+3}{2}\right)}{\Gamma\left(\frac{3}{2}\right)}
$$
This is an extension of Example $13.1 .1,$ in which the distribution was in kinetic energy $E=m v^{2} / 2,$ with $d E=m v d v$
$\boxed{\textbf{Solution}}$ 
$$\left\langle v^{n}\right\rangle=N^{-1} \int v^{n} d N$$
$$=\int v^{n} \frac{d N}{N}$$
$$=\int_{0}^{\infty} v^{n} \cdot 4 \pi\left(\frac{m}{2 \pi k T}\right)^{\frac{3}{2}} e^{\frac{m^{2}}{2 k T}} v^{2} d v$$
$$=4 \pi\left(\frac{m}{2 \pi k T}\right)^{\frac{3}{2}} \int_{0}^{\infty} v^{n} e^{\frac{m^{2}}{2 k T}} v^{n+1} v d v$$

Let $\frac{m v^{2}}{2 k T}=u^{2} .$ Then $v=\left(\frac{2 k T}{m}\right)^{\frac{1}{2}} u$ and $v d v=\frac{2 k T}{m} u d u$. As $v \rightarrow 0, \  u \rightarrow 0$ and as $v \rightarrow \infty, \  u \rightarrow \infty$. Then the above integral becomes
$$
\left\langle v^{n}\right\rangle=4 \pi\left(\frac{m}{2 \pi k T}\right)^{\frac{3}{2}} \int_{0}^{\infty} e^{-u^{2}} u^{n+1}\left(\frac{2 k T}{m}\right)^{\frac{n+1}{2}} \cdot \frac{2 k T}{m} u d u
$$
$$
=4 \pi\left(\frac{m}{2 \pi k T}\right)^{\frac{3}{2}} \cdot\left(\frac{2 k T}{m}\right)^{\frac{n+3}{2}} \int_{0}^{\infty} e^{-u^{2}} u^{n+2} d u
$$
Let $u^{2}=t \cdot$ Then $2 u d u=d t$ As $u \rightarrow 0, \  t \rightarrow 0$ and as $u \rightarrow \infty, \  t \rightarrow \infty$. As $u \rightarrow 0, \  t \rightarrow 0$ and as $u \rightarrow \infty, \  t \rightarrow \infty$.

$$
\begin{aligned}
\left\langle v^{n}\right\rangle&=4 \pi\left(\frac{m}{2 \pi k T}\right)^{\frac{3}{2}} \cdot\left(\frac{2 k T}{m}\right)^{\frac{n+3}{2}} \int_{0}^{\infty} e^{-t} t^{\frac{n+1}{2}} \frac{d t}{2} \\
&=2 \pi\left(\frac{m}{2 \pi k T}\right)^{\frac{3}{2}} \cdot\left(\frac{2 k T}{m}\right)^{\frac{n+3}{2}} \int_{0}^{\infty} e^{-t} t^{\frac{n+3}{2}} d t \\
&=2 \pi\left(\frac{m}{2 \pi k T}\right)^{\frac{3}{2}} \cdot\left(\frac{2 k T}{m}\right)^{\frac{n+3}{2}} \int_{0}^{\infty} e^{-t} t^{\frac{n+3}{2}} d t \\
&=\frac{2 \pi}{\pi \sqrt{\pi}}\left(\frac{2 k T}{m}\right)^{\frac{n+3}{2}-\frac{3}{2}} \Gamma\left(\frac{n+3}{2}\right) \\
&=\frac{2}{\sqrt{\pi}}\left(\frac{2 k T}{m}\right)^{\frac{n}{2}} \Gamma\left(\frac{n+3}{2}\right) \\
&=\left(\frac{2 k T}{m}\right)^{\frac{n}{2}} \frac{\Gamma\left(\frac{n+3}{2}\right)}{\Gamma\left(\frac{3}{2}\right)} \\
\end{aligned}
$$


since $\Gamma\left(\dfrac{3}{2}\right)=\dfrac{\sqrt{\pi}}{2}$. Hence 
$$\left\langle v^{n}\right\rangle=\left(\dfrac{2 k T}{m}\right)^{\frac{n}{2}} \frac{\Gamma\left(\frac{n+3}{2}\right)}{\Gamma\left(\frac{3}{2}\right)}$$



$\boxed{\textbf{13.1.5}}$ By transforming the integral into a gamma function, show that
$$
-\int_{0}^{1} x^{k} \ln x d x=\frac{1}{(k+1)^{2}}, \quad k>-1
$$
$\boxed{\textbf{Solution}}$ Put $x=e^{t} .$ Then $t=\ln x$ and $d x=e^{\prime} d t$. As $x \rightarrow 0, \  t \rightarrow \infty$ and as $x \rightarrow 1, t \rightarrow 0$.
$$-\int_{0}^{1} x^{k} \ln x d x$$
$$=-\int_{\infty}^{0} e^{k t} t e^{\prime} d t$$
$$=\int_{0}^{\infty} e^{(k+1) t} t d t$$
Now put $-(k+1) t=z .$ Then 
$$d t=-\frac{d z}{(k+1)} $$
As $t \rightarrow 0, \  z \rightarrow 0$ and as $t \rightarrow \infty, \  z \rightarrow 0$. Then
$$-\int_{0}^{1} x^{k} \ln x d x$$
$$=\int_{0}^{\infty} e^{(k+1) t} t d t$$
$$=\int_{0}^{\infty} e^{-z}\left(\frac{z}{-(k+1)}\right)\left(\frac{d z}{-(k+1)}\right)$$
$$=\frac{1}{(k+1)^{2}} \int_{0}^{\infty} z e^{-z} d z$$
$$=\frac{1}{(k+1)^{2}} \int_{0}^{\infty} z^{2-1} e^{-z} d z$$
$$=\frac{1}{(k+1)^{2}} \Gamma(2)$$
$$=\frac{1}{(k+1)^{2}} \cdot 1 !$$
$$=\frac{1}{(k+1)^{2}}$$
Hence
$$
-\int_{0}^{1} x^{k} \ln x d x=\frac{1}{(k+1)^{2}}, \quad k>-1
$$

$\boxed{\textbf{13.1.6}}$ Show that
$$
\int_{0}^{\infty} e^{-x^{4}} d x=\Gamma\left(\frac{5}{4}\right)
$$
$\boxed{\textbf{Solution}}$ Consider $x^{4}=t$ and put $4x^3 dx = dt$ as $t \rightarrow 0$ to $\infty, \  x \rightarrow 0$ to $\infty$ and using
$$
\int_{0}^{\infty} e^{-t} t^{z-1} d t=\Gamma (z)
$$
and
$$
z \Gamma (z)=\Gamma(z+1)
$$
the integral takes the form of

$$\begin{aligned} \frac{1}{4} \int_{0}^{\infty} e^{-t} t^{-3 / 4} d t &=\frac{1}{4} \int_{0}^{\infty} e^{-t} t^{1 / 4-1} d t \\ &=\frac{1}{4} \Gamma\left(\frac{1}{4}\right) \\ &=\Gamma\left(\frac{5}{4}\right) \end{aligned}$$



$\boxed{\textbf{13.1.7}}$ Show that
$$
\lim _{x \rightarrow 0} \frac{\Gamma(a x)}{\Gamma(x)}=\frac{1}{a}
$$
$\boxed{\textbf{Solution}}$ 
$$\begin{aligned}
\lim _{x \rightarrow 0} \frac{\Gamma(a x)}{\Gamma(x)}&=\lim _{x \rightarrow 0} \frac{\left(\frac{a x \Gamma(a x)}{a x}\right)}{\left(\frac{x \Gamma(x)}{x}\right)} \\
&=\lim _{x \rightarrow 0}\left(\frac{\Gamma(a x+1)}{\Gamma(x+1)} \cdot \frac{x}{a x}\right) \\
&=\frac{1}{a} \lim _{x \rightarrow 0} \frac{\Gamma(a x+1)}{\Gamma(x+1)}\\
&=\frac{1}{a} \frac{\Gamma(1)}{\Gamma(1)}\\
&=\frac{1}{a}
\end{aligned}
$$


$\boxed{\textbf{13.1.8}}$ Locate the poles of $\Gamma(z)$. Show that they are simple poles and determine the residues.
$\boxed{\textbf{Solution}}$
Recall that 
$$\Gamma(z)=\lim _{n \rightarrow \infty} \frac{1 \cdot 2 \cdot 3  \cdots  n}{z(z+1)(z+2) \cdots(z+n)} \cdot n^{2},$$ where $z \neq 0,-1,-2,-3, \cdots$. The denominator shows that $\Gamma(z)$ has simple poles at $z=0,-1,-2,-3, \cdots$
$$\begin{aligned}
\Gamma(z)&=\int_{0}^{\infty} e^{-t} t^{z-1} d t \\
&=\int_{0}^{1} e^{-t} t^{z-1} d t+\int_{1}^{\infty} e^{-t} t^{z-1} d t \\
&=\int_{0}^{1} t^{z-1} \sum_{n=0}^{\infty} \frac{(-t)^{n}}{n! \ } d t+\int_{1}^{\infty} e^{-t} t^{z-1} d t \\
&=\sum_{n=0}^{\infty} \frac{(-1)^{n}}{n! \ } \int_{0}^{1} t^{n+z-1} d t+\int_{1}^{\infty} e^{-t} t^{z-1} d t \\
&=\sum_{n=0}^{\infty} \frac{(-1)^{n}}{n! \ } \cdot\left[\frac{t^{n+z}}{n+z}\right]_{0}^{1}+\int_{1}^{\infty} e^{-t} t^{z-1} d t \\
&=\sum_{n=0}^{\infty} \frac{(-1)^{n}}{n! \ } \cdot\left[\frac{1}{n+z}-0\right]+\int_{1}^{\infty} e^{-t} t^{z-1} d t \\
&=\sum_{n=0}^{\infty} \frac{(-1)^{n}}{n! \ (n+z)}+\int_{1}^{\infty} e^{-t} t^{z-1} d t \\
\end{aligned}$$

The series 
$$\sum_{n=0}^{\infty} \frac{(-1)^{n}}{n! \ (n+z)}$$ 
shows that the first order poles at all negative integers $z=-n$ has respective residues 
$$\frac{(-1)^{n}}{n! \ }$$


$\boxed{\textbf{13.1.9}}$ (not solved yet.)

$\boxed{\textbf{13.1.10}}$ Show that, for integer $s$

$$\int_{0}^{\infty} x^{2 s+1} \exp \left(-a x^{2}\right) d x=\frac{s!}{2 a^{s+1}}$$
$$\int_{0}^{\infty} x^{2 s} \exp \left(-a x^{2}\right) d x=\frac{\Gamma\left(s+\frac{1}{2}\right)}{2 a^{s+1 / 2}}=\frac{(2 s-1) ! !}{2^{s+1} a^{s}} \sqrt{\frac{\pi}{a}}$$
$\boxed{\textbf{Solution}}$ For $(a)$ Put $a x^{2}=z \cdot$ Then $2 a x d x=d z$. This implies
$$
d x=\frac{d z}{2 \sqrt{a z}}
$$
As $x \rightarrow 0, \  z \rightarrow 0$ and as $x \rightarrow \infty, \  z \rightarrow \infty$.
The given integral is

$$\begin{aligned}
\int_{0}^{\infty} x^{2 s+1} \exp \left(-a x^{2}\right) d x &=\int_{0}^{\infty}\left(\sqrt{\frac{z}{a}}\right)^{2 s+1} e^{-z} \frac{d z}{2 \sqrt{a z}}\\
&=\frac{1}{2 \sqrt{a}} \int_{0}^{\infty}\left(\frac{z}{a}\right)^{\frac{2 s+1}{2}} e^{-z} z^{-\frac{1}{2}} d z \\
&=\frac{1}{2 a^{\frac{1}{2}}} \cdot \frac{1}{a^{\frac{2 s+1}{2}}} \int_{0}^{\infty} e^{-z} z^{\frac{2 s+1}{2}-\frac{1}{2}} d z \\
&=\frac{1}{2 a^{s+1}} \int_{0}^{\infty} e^{-z} z^{s} d z \\
&=\frac{1}{2 a^{s+1}} \int_{0}^{\infty} e^{-z} z^{(s+1)-1} d z \\
&=\frac{1}{2 a^{s+1}} \Gamma(s+1) \\
\end{aligned}
$$

since $s$ is an integer, therefore $\Gamma(s+1)=s! \ $. Hence 
$$\int_{0}^{\infty} x^{2 s+1} \exp \left(-a x^{2}\right) d x=\frac{s!}{2 a^{s+1}}$$ 

$\boxed{\textbf{Solution}}$ For $(b)$ Put $a x^{2}=z \cdot$ Then $2 a x d x=d z$. This implies
$$
d x=\frac{d z}{2 \sqrt{a z}}
$$
As $x \rightarrow 0, \  z \rightarrow 0$ and as $x \rightarrow \infty, \  z \rightarrow \infty$.
The given integral is

$$
\begin{aligned}
\int_{0}^{\infty} x^{2 s} \exp \left(-a x^{2}\right) d x &=\int_{0}^{\infty}\left(\sqrt{\frac{z}{a}}\right)^{2 s} e^{-z} \frac{d z}{2 \sqrt{a z}} \\
&=\frac{1}{2 \sqrt{a}} \int_{0}^{\infty}\left(\frac{z}{a}\right)^{s} e^{-z} z^{-\frac{1}{2}} d z \\
&=\frac{1}{2 a^{\frac{1}{2}}} \cdot \frac{1}{a^{s}} \int_{0}^{\infty} e^{-z} z^{s-\frac{1}{2}} d z \\
&=\frac{1}{2 a^{s+\frac{1}{2}}} \int_{0}^{\infty} e^{-z} z^{\left(s+\frac{3}{2}\right)-1} d z \\
&=\frac{1}{2 a^{s+\frac{1}{2}}} \Gamma\left(s+\frac{3}{2}\right) \\
\end{aligned}
$$

since 
$$\Gamma\left(s+\frac{1}{2}\right)=\frac{\sqrt{\pi}}{2^{s}} \cdot(2 s-1) ! !$$
$$
=\frac{(2 s-1) ! !}{2^{s+1} a^{s}} \sqrt{\frac{\pi}{a}}
$$
Thus
$$
\int_{0}^{\infty} x^{2 s} \exp \left(-a x^{2}\right) d x=\frac{\Gamma\left(s+\frac{1}{2}\right)}{2 a^{s+\frac{1}{2}}}=\frac{(2 s-1) ! !}{2 a^{s+1} a^{s}} \sqrt{\frac{\pi}{a}}
$$


$\boxed{\textbf{13.1.11}}$
Express the coefficient of the $n$ th term of the expansion of $(1+x)^{1 / 2}$ in powers of $x$

* in terms of factorials of integers,
* in terms of the double factorial (!!) functions.
 
$$
A N S . \ a_{n}=(-1)^{n+1} \frac{(2 n-3) !}{2^{2 n-2} n! \ (n-2) !}=(-1)^{n+1} \frac{(2 n-3) ! !}{(2 n) ! !},\quad n=2,3,  \cdots
$$

$\boxed{\textbf{Solution}}$ For $(a)$ the $n$ th term of the expansion of $(1+x)^{1 / 2}$ in powers of $x$ is:
$$
\begin{aligned}
a_{n} &= \binom{1/2}{1} \\
&=\frac{\frac{1}{2}\left(\frac{1}{2}-1\right)\left(\frac{1}{2}-2\right)\left(\frac{1}{2}-3\right) \cdots\left(\frac{1}{2}-(n-1)\right)}{n! \ } \\
&=\frac{\left(\frac{1}{2}\right)\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)\left(-\frac{5}{2}\right) \cdots\left(-\frac{2 n-3}{2}\right)}{n! \ } \\
&=\frac{(-1)^{n-1}}{n! \  2^{n}}[1.3 .5   \cdots (2 n-3)] \\
&=\frac{(-1)^{n+1}}{n! \  2^{n}}\left[\frac{1\cdot 2  \cdot 3  \cdot 4  \cdot 5  \cdot 6  \cdots (2 n-4) \cdot(2 n-3)}{2 \cdot 4  \cdot 6  \cdot   \cdots (2 n-4)}\right] \\
&=\frac{(-1)^{n}}{n! \  2^{n}} \cdot \frac{(2 n-3) !}{(n-2) ! 2^{n-2}} \\
&=(-1)^{n+1} \cdot \frac{(2 n-3) !}{2^{2 n-2} \cdot n! \ (n-2) !} 
\end{aligned}
$$

Therefore, 
$$
a_{n}=(-1)^{n+1} \cdot \frac{(2 n-3) !}{2^{2 n-2} n! \ (n-2) !}, \quad  n=1,2,3, \cdots
$$

$\boxed{\textbf{Solution}}$ For $(b)$ the $n$ th term expansion of $(1+x)^{1 / 2}$ 
$$\begin{aligned}
a_{n} &= \binom{-1/2}{1} \\
&=\frac{\frac{1}{2}\left(\frac{1}{2}-1\right)\left(\frac{1}{2}-2\right)\left(\frac{1}{2}-3\right) \cdots\left(\frac{1}{2}-(n-1)\right)}{n! \ } \\
&=\frac{\left(\frac{1}{2}\right)\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)\left(-\frac{5}{2}\right) \cdots\left(-\frac{2 n-3}{2}\right)}{n! \ } \\
&=\frac{(-1)^{n-1}}{n! \  2^{n}}[1 \cdot 3  \cdot 5  \cdots  \cdot(2 n-3)] \\
&=(-1)^{n+1} \cdot\left[\frac{1 \cdot 3  \cdot 5  \cdots (2 n-3)}{2 \cdot 4  \cdot 6 \cdot  \cdots 2 n}\right] \\
&=(-1)^{n+1} \cdot \frac{(2 n-3) ! !}{(2 n) ! !}
\end{aligned}
$$

Therefore
$$
a_{n}=(-1)^{n+1} \cdot \frac{(2 n-3) ! !}{(2 n) ! !}, \quad \text { for } n=1,2,3, \cdots
$$


$\boxed{\textbf{13.1.12}}$
Express the coefficient of the $n$ th term of the expansion of $(1+x)^{-1 / 2}$ in powers of $x$

* in terms of the factorials of integers,
* in terms of the double factorial (!!) functions.

$$
A N S . \quad a_{n}=(-1)^{n} \frac{(2 n) !}{2^{2 n}(n! \ )^{2}}=(-1)^{n} \frac{(2 n-1) ! !}{(2 n) ! !}, \quad n=1,2,3  \cdots
$$

$\boxed{\textbf{Solution}}$ For $(a)$ the $n$ th term of the expansion of $(1+x)^{-1 / 2}$ in powers of $x$ is:
$$
\begin{aligned}
a_{n} &= \binom{-1/2}{n-1} \\
&=\frac{-\frac{1}{2}\left(-\frac{1}{2}-1\right)\left(-\frac{1}{2}-2\right)\left(-\frac{1}{2}-3\right) \cdots\left(-\frac{1}{2}-(n-1)\right)}{n! \ } \\
&=\frac{\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)\left(-\frac{5}{2}\right) \cdots\left(-\frac{2 n-1}{2}\right)}{n! \ } \\
&=\frac{(-1)^{n}}{n! \  2^{n}}[1 \cdot 3  \cdot 5  \cdot   \cdots (2 n-1)] \\
&=\frac{(-1)^{n}}{n! \  2^{n}}\left[\frac{1 \cdot 2  \cdot 3  \cdot 4  \cdot 5  \cdot 6  \cdot   \cdots (2 n-1) \cdot 2 n}{2 \cdot 4  \cdot 6  \cdot   \cdots 2 n}\right] \\
&=\frac{(-1)^{n}}{n! \  2^{n}} \cdot \frac{(2 n) !}{n! \  2^{n}} \\
&=(-1)^{n} \cdot \frac{(2 n) !}{2^{2 n} \cdot(n! \ )^{2}} \\
\end{aligned}
$$

Therefore, 
$$
a_{n}=(-1)^{n} \cdot \frac{(2 n) !}{2^{2 n} \cdot(n! \ )^{2}}, \quad \text { for } n=1,2,3, \cdots
$$

$\boxed{\textbf{Solution}}$ For $(b)$ the $n$ th term expansion of $(1+x)^{-1 / 2}$ in powers of $x$ in terms of the double factorial $(!!)$ functions.
$$
\begin{aligned}
a_{n}&=\binom{-1/2}{n-1} \\
&=\frac{-\frac{1}{2}\left(-\frac{1}{2}-1\right)\left(-\frac{1}{2}-2\right)\left(-\frac{1}{2}-3\right) \cdots\left(-\frac{1}{2}-(n-1)\right)}{n! \ } \\
&=\frac{\left(-\frac{1}{2}\right)\left(-\frac{3}{2}\right)\left(-\frac{5}{2}\right) \cdots\left(-\frac{2 n-1}{2}\right)}{n! \ } \\
&=\frac{(-1)^{n}}{n! \  2^{n}}[1 \cdot 3  \cdot 5   \cdots (2 n-1)] \\
&=(-1)^{n} \cdot\left[\frac{1 \cdot 3  \cdot 5   \cdots (2 n-1)}{2 \cdot 4  \cdot 6  \cdot   \cdots 2 n}\right] \\
&=(-1)^{n} \cdot \frac{(2 n-1) ! !}{(2 n) ! !} 
\end{aligned}
$$


Therefore
$$
a_{n}=(-1)^{n} \cdot \frac{(2 n-1) ! !}{(2 n) ! !}, \quad \text { for } n=1,2,3, \cdots
$$

$\boxed{\textbf{13.1.14}}$

* Show that $\Gamma\left(\frac{1}{2}-n\right) \Gamma\left(\frac{1}{2}+n\right)=(-1)^{n} \pi,$ where $n$ is an integer. 
* Express $\Gamma\left(\frac{1}{2}+n\right)$ and $\Gamma\left(\frac{1}{2}-n\right)$ separately in terms of $\pi^{1 / 2}$ and a double factorial function.

$$
A N S . \quad \Gamma\left(\frac{1}{2}+n\right)=\frac{(2 n-1) ! !}{2^{n}} \pi^{1 / 2}
$$

$\boxed{\textbf{Solution}}$ For $(a)$ recall that 
$$\Gamma(z) \Gamma(1-z)=\frac{\pi}{\sin \pi z}$$
Putting $z=\frac{1}{2}+n$ in the above relation, it becomes
$$
\Gamma\left(\frac{1}{2}+n\right) \Gamma\left(1-\frac{1}{2}-n\right)=\frac{\pi}{\sin \left[\pi\left(\frac{1}{2}+n\right)\right]}
$$
$$
=\frac{\pi}{\cos (n \pi)}
$$
$$
=\frac{\pi}{(-1)^{n}}
$$
since $\cos (n \pi)=(-1)^{n}$ and
$$
=(-1)^{n} \pi
$$
Therefore 
$$\Gamma\left(\frac{1}{2}-n\right) \Gamma\left(\frac{1}{2}+n\right)=(-1)^{n} \pi$$ where $n$ is an integer.

$\boxed{\textbf{Solution}}$ For $(b)$ recall the Legendre's duplication formula,
$$\Gamma(1+z) \Gamma\left(z+\frac{1}{2}\right)=2^{-2 z} \sqrt{\pi} \Gamma(2 z+1)$$
Putting $z=n$ in the above relation, it becomes
$$
\begin{aligned}
\Gamma(1+n) \Gamma\left(n+\frac{1}{2}\right)&=2^{-2 n} \sqrt{\pi} \Gamma(2 n+1) \\
&=\frac{2^{-2 n} \sqrt{\pi} \Gamma(2 n+1)}{\Gamma(1+n)} \\
&=\frac{\sqrt{\pi}}{2^{2 n}} \cdot \frac{(2 n) !}{n! \ } \\
&=\frac{\sqrt{\pi}}{2^{2 n}} \cdot \frac{(1 \cdot 2  \cdot 3  \cdot 4  \cdot 5   \cdots   \cdot 2 n)}{(1 \cdot 2  \cdot 3  \cdots n)} \\
&=\frac{\sqrt{\pi}}{2^{n}} \cdot \frac{(1 \cdot 2  \cdot 3  \cdot 4  \cdot 5   \cdots   \cdot 2 n)}{(2 \cdot 4  \cdot 6   \cdots   \cdot 2 n)} \\
&=\frac{\sqrt{\pi}}{2^{n}} \cdot[1 \cdot 3  \cdot 5   \cdots (2 n-1)] \\
&=\frac{\sqrt{\pi}}{2^{n}} \cdot(2 n-1) ! ! \cdots 
\end{aligned}
$$

From part $(a)$ 
$$
\Gamma\left(\frac{1}{2}-n\right) \Gamma\left(\frac{1}{2}+n\right)=(-1)^{n} \pi
$$
$$
\begin{aligned}
\Gamma\left(\frac{1}{2}-n\right)&=\frac{(-1)^{n} \pi}{\Gamma\left(\frac{1}{2}+n\right)} \\
&=\frac{(-1)^{n} \pi}{\left(\frac{\sqrt{\pi}}{2^{n}} \cdot(2 n-1) ! !\right)} \\
&=\frac{(-1)^{n} \cdot 2^{n} \sqrt{\pi}}{(2 n-1) ! !} \\
&=\frac{\sqrt{\pi}}{2^{n}} \cdot(2 n-1) ! ! \quad \text { and } \quad \Gamma\left(\frac{1}{2}-n\right)=\frac{(-1)^{n} \cdot 2^{n} \sqrt{\pi}}{(2 n-1) ! !} \\
\end{aligned}
$$



$\boxed{\textbf{13.1.16}}$ Prove that 

$$|\Gamma(\alpha+i \beta)|=|\Gamma(\alpha)| \prod_{n=0}^{\infty}\left[1+\frac{\beta^{2}}{(\alpha+n)^{2}}\right]^{-1 / 2}$$

$\boxed{\textbf{Solution}}$ Recall 
$$
\frac{1}{\Gamma(z)}=z e^{\gamma z} \prod_{n=1}^{\infty}\left(1+\frac{z}{n}\right) e^{-\frac{z}{n}}
$$
Putting $z=\alpha+i \beta$ and $z=\alpha-i \beta$ successively in the above relation, it becomes
$$
\frac{1}{\Gamma(\alpha+i \beta)}=(\alpha+i \beta) e^{\gamma(\alpha+i \beta)} \prod_{n=1}^{\infty}\left(1+\frac{\alpha+i \beta}{n}\right) e^{-\frac{a+i \beta}{n}}
$$
and 
$$
\frac{1}{\Gamma(\alpha-i \beta)}=(\alpha-i \beta) e^{\gamma(\alpha-i \beta)} \prod_{n=1}^{\infty}\left(1+\frac{\alpha-i \beta}{n}\right) e^{\frac{a-i \beta}{n}}
$$

Multiplying these equations it becomes

$$
\begin{aligned}
\frac{1}{\Gamma(\alpha+i \beta)} \cdot \frac{1}{\Gamma(\alpha-i \beta)}&=(\alpha+i \beta) e^{\gamma(a+i \beta)} \cdot(\alpha-i \beta) e^{\gamma(a-i \beta)} \\
&\times \prod_{n=1}^{\infty}\left[\left(1+\frac{\alpha+i \beta}{n}\right) e^{\frac{a+i \beta}{n}} \cdot\left(1+\frac{\alpha-i \beta}{n}\right) e^{\frac{\alpha-i \beta}{n}}\right] \\
\frac{1}{\|\Gamma(\alpha+i \beta)\|^{2}}&=\left(\alpha^{2}+\beta^{2}\right) e^{2\gamma \alpha} \prod_{n=1}^{\infty} e^{-\frac{2 a}{n}}\left[\left(1+\frac{\alpha+i \beta}{n}\right) \cdot\left(1+\frac{\alpha-i \beta}{n}\right)\right] \\
&=\left(\alpha^{2}+\beta^{2}\right) e^{2 \gamma a} \prod_{n=1}^{\infty}\left[e^{-\frac{2 a}{n}} \cdot \frac{\left(1+\frac{\alpha+i \beta}{n}\right) \cdot\left(1+\frac{\alpha-i \beta}{n}\right)}{\left(1+\frac{\alpha}{n}\right)^{2}} \cdot\left(1+\frac{\alpha}{n}\right)^{2}\right] \\
&=\left(\alpha^{2}+\beta^{2}\right) e^{2 \gamma a} \prod_{n=1}^{\infty}\left[e^{-\frac{2 a}{n}} \cdot \frac{\left(1+\frac{\alpha+i \beta}{n}\right) \cdot\left(1+\frac{\alpha-i \beta}{n}\right)}{\left(1+\frac{\alpha}{n}\right)^{2}} \cdot\left(1+\frac{\alpha}{n}\right)^{2}\right] \\
&=\left(\frac{\alpha^{2}+\beta^{2}}{\alpha^{2}}\right)\left(\alpha e^{\gamma \alpha} \prod_{n=1}^{\infty}\left[e^{-\frac{a}{n}} \cdot\left(1+\frac{\alpha}{n}\right)\right]\right)^{2} \prod_{n=1}^{\infty}\left[\frac{\left(1+\frac{2 \alpha}{n}+\frac{\alpha^{2}+\beta^{2}}{n^{2}}\right)}{\frac{(n+\alpha)^{2}}{n^{2}}}\right] \\
&=\left(1+\frac{\beta^{2}}{\alpha^{2}}\right) \frac{1}{\Gamma(\alpha)^{2}} \prod_{n=1}^{\infty}\left[\frac{\left(1+2 \alpha n+\alpha^{2}+\beta^{2}\right)}{(n+\alpha)^{2}}\right] \\
&=\frac{1}{\Gamma(\alpha)^{2}} \cdot\left(1+\frac{\beta^{2}}{\alpha^{2}}\right) \prod_{n=1}^{\infty}\left[\frac{(n+\alpha)^{2}+\beta^{2}}{(n+\alpha)^{2}}\right] \\
&=\frac{1}{\Gamma(\alpha)^{2}} \cdot\left(1+\frac{\beta^{2}}{\alpha^{2}}\right) \prod_{n=1}^{\infty}\left[1+\frac{\beta^{2}}{(n+\alpha)^{2}}\right] \\
&=\frac{1}{\Gamma(\alpha)^{2}} \prod_{n=0}^{\infty}\left[1+\frac{\beta^{2}}{(n+\alpha)^{2}}\right] \\
\end{aligned}
$$
Hence

$$\frac{1}{\|\Gamma(\alpha+i \beta)\|^{2}}=\frac{1}{\Gamma(\alpha)^{2}} \prod_{n=0}^{\infty}\left[1+\frac{\beta^{2}}{(n+\alpha)^{2}}\right]$$

$$\frac{1}{\|\Gamma(\alpha+i \beta)\|}=\frac{1}{\|\Gamma(\alpha)\|} \prod_{n=0}^{\infty}\left[1+\frac{\beta^{2}}{(n+\alpha)^{2}}\right]^{\frac{1}{2}}$$

$$|\Gamma(\alpha+i \beta)|=|\Gamma(\alpha)| \prod_{n=0}^{\infty}\left[1+\frac{\beta^{2}}{(\alpha+n)^{2}}\right]^{-\frac{1}{2}}$$

$\boxed{\textbf{13.1.17}}$ Show that for $n$, a positive integer,

$$|\Gamma(n+i b+1)|=\left(\frac{\pi b}{\sinh \pi b}\right)^{1 / 2} \prod_{s=1}^{n}\left(s^{2}+b^{2}\right)^{1 / 2}$$


$\boxed{\textbf{Solution}}$ Recall 
$$
\frac{1}{\Gamma(z)}=z e^{\gamma z} \prod_{n=1}^{\infty}\left(1+\frac{z}{n}\right) e^{-\frac{z}{n}}
$$
Putting $z=\alpha+i \beta$ and $z=\alpha-i \beta$ successively in the above relation, it becomes
$$
\frac{1}{\Gamma(\alpha+i \beta)}=(\alpha+i \beta) e^{\gamma(\alpha+i \beta)} \prod_{n=1}^{\infty}\left(1+\frac{\alpha+i \beta}{n}\right) e^{-\frac{a+i \beta}{n}}
$$
and 
$$
\frac{1}{\Gamma(\alpha-i \beta)}=(\alpha-i \beta) e^{\gamma(\alpha-i \beta)} \prod_{n=1}^{\infty}\left(1+\frac{\alpha-i \beta}{n}\right) e^{\frac{a-i \beta}{n}}
$$
Multiplying these equations it becomes
$$
\begin{aligned}
\frac{1}{\Gamma(\alpha+i \beta)} \cdot \frac{1}{\Gamma(\alpha-i \beta)}&=(\alpha+i \beta) e^{\gamma(a+i \beta)} \cdot(\alpha-i \beta) e^{\gamma(a-i \beta)} \\
&\times \prod_{n=1}^{\infty}\left[\left(1+\frac{\alpha+i \beta}{n}\right) e^{\frac{a+i \beta}{n}} \cdot\left(1+\frac{\alpha-i \beta}{n}\right) e^{\frac{\alpha-i \beta}{n}}\right] \\
\frac{1}{\|\Gamma(\alpha+i \beta)\|^{2}}&=\left(\alpha^{2}+\beta^{2}\right) e^{2\gamma \alpha} \prod_{n=1}^{\infty} e^{-\frac{2 a}{n}}\left[\left(1+\frac{\alpha+i \beta}{n}\right) \cdot\left(1+\frac{\alpha-i \beta}{n}\right)\right] \\
&=\left(\alpha^{2}+\beta^{2}\right) e^{2 \gamma a} \prod_{n=1}^{\infty}\left[e^{-\frac{2 a}{n}} \cdot \frac{\left(1+\frac{\alpha+i \beta}{n}\right) \cdot\left(1+\frac{\alpha-i \beta}{n}\right)}{\left(1+\frac{\alpha}{n}\right)^{2}} \cdot\left(1+\frac{\alpha}{n}\right)^{2}\right] \\
&=\left(\alpha^{2}+\beta^{2}\right) e^{2 \gamma a} \prod_{n=1}^{\infty}\left[e^{-\frac{2 a}{n}} \cdot \frac{\left(1+\frac{\alpha+i \beta}{n}\right) \cdot\left(1+\frac{\alpha-i \beta}{n}\right)}{\left(1+\frac{\alpha}{n}\right)^{2}} \cdot\left(1+\frac{\alpha}{n}\right)^{2}\right] \\
&=\left(\frac{\alpha^{2}+\beta^{2}}{\alpha^{2}}\right)\left(\alpha e^{\gamma \alpha} \prod_{n=1}^{\infty}\left[e^{-\frac{a}{n}} \cdot\left(1+\frac{\alpha}{n}\right)\right]\right)^{2} \prod_{n=1}^{\infty}\left[\frac{\left(1+\frac{2 \alpha}{n}+\frac{\alpha^{2}+\beta^{2}}{n^{2}}\right)}{\frac{(n+\alpha)^{2}}{n^{2}}}\right] \\
&=\left(1+\frac{\beta^{2}}{\alpha^{2}}\right) \frac{1}{\Gamma(\alpha)^{2}} \prod_{n=1}^{\infty}\left[\frac{\left(1+2 \alpha n+\alpha^{2}+\beta^{2}\right)}{(n+\alpha)^{2}}\right] \\
&=\frac{1}{\Gamma(\alpha)^{2}} \cdot\left(1+\frac{\beta^{2}}{\alpha^{2}}\right) \prod_{n=1}^{\infty}\left[\frac{(n+\alpha)^{2}+\beta^{2}}{(n+\alpha)^{2}}\right] \\
&=\frac{1}{\Gamma(\alpha)^{2}} \cdot\left(1+\frac{\beta^{2}}{\alpha^{2}}\right) \prod_{n=1}^{\infty}\left[1+\frac{\beta^{2}}{(n+\alpha)^{2}}\right] \\
&=\frac{1}{\Gamma(\alpha)^{2}} \prod_{n=0}^{\infty}\left[1+\frac{\beta^{2}}{(n+\alpha)^{2}}\right] \\
\end{aligned}
$$

Hence

$$
\frac{1}{\|\Gamma(\alpha+i \beta)\|^{2}}=\frac{1}{\Gamma(\alpha)^{2}} \prod_{n=0}^{\infty}\left[1+\frac{\beta^{2}}{(n+\alpha)^{2}}\right]
$$

Now put $\alpha=1$ and $\beta=b$ in the above identity. Then it becomes

$$
\begin{aligned}
\frac{1}{\|\Gamma(1+i b)\|^{2}}&=\frac{1}{\Gamma(1)^{2}} \prod_{n=0}^{\infty}\left[1+\frac{b^{2}}{(n+1)^{2}}\right] \\
&=\prod_{n=0}^{\infty}\left[1+\frac{b^{2}}{(n+1)^{2}}\right], \quad \text { as } \quad \Gamma(1)=1 \\
&=\prod_{n=0}^{\infty}\left[1-\frac{(i b \pi)^{2}}{(n+1)^{2} \pi^{2}}\right] \\
&=\prod_{n=1}^{\infty}\left[1-\frac{(i b \pi)^{2}}{n^{2} \pi^{2}}\right] \\
&=\frac{1}{(i b \pi)}\left\{(i b \pi) \prod_{n=1}^{\infty}\left[1-\frac{(i b \pi)^{2}}{n^{2} \pi^{2}}\right]\right\} \\
&=\frac{1}{i b \pi} \cdot \sin (i b \pi) \\
\end{aligned}
$$

Using the identy
$$
\sin z=z \prod_{n=1}^{\infty}\left[1-\frac{z^{2}}{n^{2} \pi^{2}}\right] \quad \text{for} \quad z=ib\pi
$$
$$=\frac{1}{i b \pi} \cdot i \sinh (b \pi)$$
$$=\frac{\sinh (b \pi)}{b \pi}$$
$$\frac{1}{\|\Gamma(1+i b)\|^{2}}=\frac{\sinh (b \pi)}{b \pi}$$
$$|\Gamma(1+i b)|^{2}=\frac{b \pi}{\sinh (b \pi)} .$$
since $n$ is an integer, therefore

$$
\begin{aligned}
\Gamma(n+i b+1)&=\Gamma(\{1+i b+(n-1)\}+1) \\
&=\{1+i b+(n-1)\} \Gamma(\{1+i b+(n-1)\}) \\
&(1+i b)(2+i b)(3+i b) \cdots(n+i b) \Gamma(1+i b) \\
\Gamma(n+i b+1)&=(1+i b)(2+i b)(3+i b) \cdots(n+i b) \Gamma(1+i b) \\
\Gamma(n-i b+1)&=(1-i b)(2-i b)(3-i b) \cdots(n-i b) \Gamma(1-i b) \\
\|\Gamma(n+i b+1)\|^{2}&=\Gamma(n+i b+1) \Gamma(n-i b+1) \\
&=(1+i b)(2+i b)(3+i b) \cdots(n+i b) \Gamma(1+i b) \times(1-i b)(2-i b)(3-i b) \cdots(n-i b) \Gamma(1-i b) \\
&=\{(1+i b)(1-i b)\}\{(2+i b)(2-i b)\}\{(3+i b)(3-i b)\} \cdots\{(n+i b)(n-i b)\} \Gamma(1+i b) \Gamma(1-i b) \\
&=\left(1^{2}+b^{2}\right)\left(2^{2}+b^{2}\right)\left(3^{2}+b^{2}\right) \cdots\left(n^{2}+b^{2}\right)\|\Gamma(1+i b)\|^{2} \\
&=\prod_{s=1}^{n}\left(s^{2}+b^{2}\right) \times \frac{b \pi}{\sinh (b \pi)} \\
\end{aligned}
$$


Hence 

$$|\Gamma(n+i b+1)|^{2}=\prod_{s=1}^{n}\left(s^{2}+b^{2}\right) \times \frac{b \pi}{\sinh (b \pi)}$$
This gives 
$$|\Gamma(n+i b+1)|=\left(\frac{b \pi}{\sinh (b \pi)}\right)^{\frac{1}{2}} \prod_{s=1}^{n}\left(s^{2}+b^{2}\right)^{\frac{1}{2}} $$


$\boxed{\textbf{13.1.18}}$ Show that for all real values of $x$ and $y,|\Gamma(x)| \geq|\Gamma(x+i y)|$

$\boxed{\textbf{Solution}}$ Recall 
$$
\frac{1}{\Gamma(z)}=z e^{\gamma z} \prod_{n=1}^{\infty}\left(1+\frac{z}{n}\right) e^{-\frac{z}{n}}
$$
Putting $z=\alpha+i \beta$ and $z=\alpha-i \beta$ successively in the above relation, it becomes
$$
\frac{1}{\Gamma(\alpha+i \beta)}=(\alpha+i \beta) e^{\gamma(\alpha+i \beta)} \prod_{n=1}^{\infty}\left(1+\frac{\alpha+i \beta}{n}\right) e^{-\frac{a+i \beta}{n}}
$$
and 
$$
\frac{1}{\Gamma(\alpha-i \beta)}=(\alpha-i \beta) e^{\gamma(\alpha-i \beta)} \prod_{n=1}^{\infty}\left(1+\frac{\alpha-i \beta}{n}\right) e^{\frac{a-i \beta}{n}}
$$
Multiplying these equations it becomes
$$
\begin{aligned}
\frac{1}{\Gamma(\alpha+i \beta)} \cdot \frac{1}{\Gamma(\alpha-i \beta)}&=(\alpha+i \beta) e^{\gamma(a+i \beta)} \cdot(\alpha-i \beta) e^{\gamma(a-i \beta)} \\
&\times \prod_{n=1}^{\infty}\left[\left(1+\frac{\alpha+i \beta}{n}\right) e^{\frac{a+i \beta}{n}} \cdot\left(1+\frac{\alpha-i \beta}{n}\right) e^{\frac{\alpha-i \beta}{n}}\right] \\
\frac{1}{\|\Gamma(\alpha+i \beta)\|^{2}}&=\left(\alpha^{2}+\beta^{2}\right) e^{2\gamma \alpha} \prod_{n=1}^{\infty} e^{-\frac{2 a}{n}}\left[\left(1+\frac{\alpha+i \beta}{n}\right) \cdot\left(1+\frac{\alpha-i \beta}{n}\right)\right] \\
&=\left(\alpha^{2}+\beta^{2}\right) e^{2 \gamma a} \prod_{n=1}^{\infty}\left[e^{-\frac{2 a}{n}} \cdot \frac{\left(1+\frac{\alpha+i \beta}{n}\right) \cdot\left(1+\frac{\alpha-i \beta}{n}\right)}{\left(1+\frac{\alpha}{n}\right)^{2}} \cdot\left(1+\frac{\alpha}{n}\right)^{2}\right] \\
&=\left(\alpha^{2}+\beta^{2}\right) e^{2 \gamma a} \prod_{n=1}^{\infty}\left[e^{-\frac{2 a}{n}} \cdot \frac{\left(1+\frac{\alpha+i \beta}{n}\right) \cdot\left(1+\frac{\alpha-i \beta}{n}\right)}{\left(1+\frac{\alpha}{n}\right)^{2}} \cdot\left(1+\frac{\alpha}{n}\right)^{2}\right] \\
&=\left(\frac{\alpha^{2}+\beta^{2}}{\alpha^{2}}\right)\left(\alpha e^{\gamma \alpha} \prod_{n=1}^{\infty}\left[e^{-\frac{a}{n}} \cdot\left(1+\frac{\alpha}{n}\right)\right]\right)^{2} \prod_{n=1}^{\infty}\left[\frac{\left(1+\frac{2 \alpha}{n}+\frac{\alpha^{2}+\beta^{2}}{n^{2}}\right)}{\frac{(n+\alpha)^{2}}{n^{2}}}\right] \\
&=\left(1+\frac{\beta^{2}}{\alpha^{2}}\right) \frac{1}{\Gamma(\alpha)^{2}} \prod_{n=1}^{\infty}\left[\frac{\left(1+2 \alpha n+\alpha^{2}+\beta^{2}\right)}{(n+\alpha)^{2}}\right] \\
&=\frac{1}{\Gamma(\alpha)^{2}} \cdot\left(1+\frac{\beta^{2}}{\alpha^{2}}\right) \prod_{n=1}^{\infty}\left[\frac{(n+\alpha)^{2}+\beta^{2}}{(n+\alpha)^{2}}\right] \\
&=\frac{1}{\Gamma(\alpha)^{2}} \cdot\left(1+\frac{\beta^{2}}{\alpha^{2}}\right) \prod_{n=1}^{\infty}\left[1+\frac{\beta^{2}}{(n+\alpha)^{2}}\right] \\
&=\frac{1}{\Gamma(\alpha)^{2}} \prod_{n=0}^{\infty}\left[1+\frac{\beta^{2}}{(n+\alpha)^{2}}\right] \\
\end{aligned}
$$

Hence

$$
\frac{1}{\|\Gamma(\alpha+i \beta)\|^{2}}=\frac{1}{\Gamma(\alpha)^{2}} \prod_{n=0}^{\infty}\left[1+\frac{\beta^{2}}{(n+\alpha)^{2}}\right]
$$

Now put $\alpha=x$ and $\beta=y$ in the above identity. Then it becomes

$$
\frac{1}{\|\Gamma(x+i y)\|^{2}}=\frac{1}{\Gamma(x)^{2}} \prod_{n=0}^{\infty}\left[1+\frac{\beta^{2}}{(n+x)^{2}}\right]
$$
$$
\left|\frac{\Gamma(x)}{\Gamma(x+i y)}\right|^{2}=\prod_{n=0}^{\infty}\left[1+\frac{\beta^{2}}{(n+x)^{2}}\right]
$$
$$
\left|\frac{\Gamma(x)}{\Gamma(x+i y)}\right|^{2} \geq 1, \quad \text { since }\quad 1+\frac{\beta^{2}}{(n+x)^{2}} \geq 1
$$
$$\left|\frac{\Gamma(x)}{\Gamma(x+i y)}\right| \geq 1$$
$$|\Gamma(x)| \geq|\Gamma(x+i y)|$$
Hence is proved



$\boxed{\textbf{13.1.19}}$ Show that 
$$\left|\Gamma(\frac{1}{2}+i y)\right|^{2}=\frac{\pi}{\cosh \pi y}$$

$\boxed{\textbf{Solution}}$ Recall 
$$
\frac{1}{\Gamma(z)}=z e^{\gamma z} \prod_{n=1}^{\infty}\left(1+\frac{z}{n}\right) e^{-\frac{z}{n}}
$$
Putting $z=\alpha+i \beta$ and $z=\alpha-i \beta$ successively in the above relation, it becomes
$$
\frac{1}{\Gamma(\alpha+i \beta)}=(\alpha+i \beta) e^{\gamma(\alpha+i \beta)} \prod_{n=1}^{\infty}\left(1+\frac{\alpha+i \beta}{n}\right) e^{-\frac{a+i \beta}{n}}
$$
and 
$$
\frac{1}{\Gamma(\alpha-i \beta)}=(\alpha-i \beta) e^{\gamma(\alpha-i \beta)} \prod_{n=1}^{\infty}\left(1+\frac{\alpha-i \beta}{n}\right) e^{\frac{a-i \beta}{n}}
$$
Multiplying these equations it becomes

$$
\begin{aligned}
\frac{1}{\Gamma(\alpha+i \beta)} \cdot \frac{1}{\Gamma(\alpha-i \beta)}&=(\alpha+i \beta) e^{\gamma(a+i \beta)} \cdot(\alpha-i \beta) e^{\gamma(a-i \beta)} \\
&\times \prod_{n=1}^{\infty}\left[\left(1+\frac{\alpha+i \beta}{n}\right) e^{\frac{a+i \beta}{n}} \cdot\left(1+\frac{\alpha-i \beta}{n}\right) e^{\frac{\alpha-i \beta}{n}}\right] \\
\frac{1}{\|\Gamma(\alpha+i \beta)\|^{2}}&=\left(\alpha^{2}+\beta^{2}\right) e^{2\gamma \alpha} \prod_{n=1}^{\infty} e^{-\frac{2 a}{n}}\left[\left(1+\frac{\alpha+i \beta}{n}\right) \cdot\left(1+\frac{\alpha-i \beta}{n}\right)\right] \\
&=\left(\alpha^{2}+\beta^{2}\right) e^{2 \gamma a} \prod_{n=1}^{\infty}\left[e^{-\frac{2 a}{n}} \cdot \frac{\left(1+\frac{\alpha+i \beta}{n}\right) \cdot\left(1+\frac{\alpha-i \beta}{n}\right)}{\left(1+\frac{\alpha}{n}\right)^{2}} \cdot\left(1+\frac{\alpha}{n}\right)^{2}\right] \\
&=\left(\alpha^{2}+\beta^{2}\right) e^{2 \gamma a} \prod_{n=1}^{\infty}\left[e^{-\frac{2 a}{n}} \cdot \frac{\left(1+\frac{\alpha+i \beta}{n}\right) \cdot\left(1+\frac{\alpha-i \beta}{n}\right)}{\left(1+\frac{\alpha}{n}\right)^{2}} \cdot\left(1+\frac{\alpha}{n}\right)^{2}\right] \\
&=\left(\frac{\alpha^{2}+\beta^{2}}{\alpha^{2}}\right)\left(\alpha e^{\gamma \alpha} \prod_{n=1}^{\infty}\left[e^{-\frac{a}{n}} \cdot\left(1+\frac{\alpha}{n}\right)\right]\right)^{2} \prod_{n=1}^{\infty}\left[\frac{\left(1+\frac{2 \alpha}{n}+\frac{\alpha^{2}+\beta^{2}}{n^{2}}\right)}{\frac{(n+\alpha)^{2}}{n^{2}}}\right] \\
&=\left(1+\frac{\beta^{2}}{\alpha^{2}}\right) \frac{1}{\Gamma(\alpha)^{2}} \prod_{n=1}^{\infty}\left[\frac{\left(1+2 \alpha n+\alpha^{2}+\beta^{2}\right)}{(n+\alpha)^{2}}\right] \\
&=\frac{1}{\Gamma(\alpha)^{2}} \cdot\left(1+\frac{\beta^{2}}{\alpha^{2}}\right) \prod_{n=1}^{\infty}\left[\frac{(n+\alpha)^{2}+\beta^{2}}{(n+\alpha)^{2}}\right] \\
&=\frac{1}{\Gamma(\alpha)^{2}} \cdot\left(1+\frac{\beta^{2}}{\alpha^{2}}\right) \prod_{n=1}^{\infty}\left[1+\frac{\beta^{2}}{(n+\alpha)^{2}}\right] \\
&=\frac{1}{\Gamma(\alpha)^{2}} \prod_{n=0}^{\infty}\left[1+\frac{\beta^{2}}{(n+\alpha)^{2}}\right] \\
\end{aligned}
$$

Hence
$$
\frac{1}{\|\Gamma(\alpha+i \beta)\|^{2}}=\frac{1}{\Gamma(\alpha)^{2}} \prod_{n=0}^{\infty}\left[1+\frac{\beta^{2}}{(n+\alpha)^{2}}\right]
$$

Now put $\alpha=\frac{1}{2}$ and $\beta=y$ in the above identity. Then it becomes
$$
\frac{1}{\left|\Gamma\left(\frac{1}{2}+i y\right)\right|^{2}}=\frac{1}{\Gamma\left(\frac{1}{2}\right)^{2}} \prod_{n=0}^{\infty}\left[1+\frac{y^{2}}{\left(n+\frac{1}{2}\right)^{2}}\right]
$$
$$
\frac{1}{\left|\Gamma\left(\frac{1}{2}+i y\right)\right|^{2}}=\frac{1}{\pi} \prod_{n=0}^{\infty}\left[1+\frac{y^{2}}{\left(n+\frac{1}{2}\right)^{2}}\right]
$$
since $\Gamma\left(\frac{1}{2}\right)=\sqrt{\pi}$
$$
\frac{1}{\left|\Gamma\left(\frac{1}{2}+i y\right)\right|^{2}}=\frac{1}{\pi} \prod_{n=0}^{\infty}\left[1+\frac{y^{2}}{\left(n+\frac{1}{2}\right)^{2}}\right]
$$
Recall
$$
\cos z=\prod_{n=1}^{\infty}\left[1-\frac{z^{2}}{\left(n-\frac{1}{2}\right)^{2} \pi^{2}}\right]
$$
and putting $z=i \pi y$ it becomes
$$
\cos (i \pi y)=\prod_{n=1}^{\infty}\left[1-\frac{i^{2} \pi^{2} y^{2}}{\left(n-\frac{1}{2}\right)^{2} \pi^{2}}\right]
$$
$$
\cosh (\pi y)=\prod_{n=1}^{\infty}\left[1+\frac{y^{2}}{\left(n-\frac{1}{2}\right)^{2}}\right]
$$
$$
\cosh (\pi y)=\prod_{n=0}^{\infty}\left[1+\frac{y^{2}}{\left(n+1-\frac{1}{2}\right)^{2}}\right]
$$
$$
\cosh (\pi y)=\prod_{n=0}^{\infty}\left[1+\frac{y^{2}}{\left(n+\frac{1}{2}\right)^{2}}\right]
$$
$$
\frac{1}{\left|\Gamma\left(\frac{1}{2}+i y\right)\right|^{2}}=\frac{1}{\pi} \cosh (\pi y)
$$

\boxed{\textbf{13.1.20}}
The probability density associated with the normal distribution of statistics is given by
$$
f(x)=\frac{1}{\sigma(2 \pi)^{1 / 2}} \exp \left[-\frac{(x-\mu)^{2}}{2 \sigma^{2}}\right]
$$
with $(-\infty, \infty)$ for the range of $x$. Show that
(a) 

* $\langle x\rangle,$ the mean value of $x,$ is equal to $\mu$
* The standard deviation $\left(\left\langle x^{2}\right\rangle-\langle x\rangle^{2}\right)^{1 / 2}$ is given by $\sigma$.


$\boxed{\textbf{Solution}}$ For $(a)$ For the mean
$$
\begin{aligned}
\langle x\rangle&=\int_{-\infty}^{\infty} x f(x) d x \\
&=\int_{-\infty}^{\infty} x \cdot \frac{1}{\sigma(2 \pi)^{\frac{1}{2}}} \exp \left[-\frac{(x-\mu)^{2}}{2 \sigma^{2}}\right] d x \\
&=\frac{1}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{-\infty}^{\infty} x e^{\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x \\
\end{aligned}
$$

Put $x-\mu=y .$ Then $d x=d y .$ As $x \rightarrow 0, \  y \rightarrow 0$ and $x \rightarrow \infty, \  y \rightarrow \infty$.

$$
\begin{aligned}
\langle x\rangle&=\frac{1}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{-\infty}^{\infty} x e^{\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x \\
&=\frac{1}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{-\infty}^{\infty}(\mu+y) e^{-\frac{y^{2}}{2 \sigma^{2}}} d y \\
&=\frac{1}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{-\infty}^{\infty}(\mu+y) e^{\frac{y^{2}}{2 \sigma^{2}}} d y \\
&=\frac{\mu}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{-\infty}^{\infty} e^{-\frac{y^{2}}{2 \sigma^{2}}} d y+\frac{1}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{-\infty}^{\infty} y e^{-\frac{y^{2}}{2 \sigma^{2}}} d y \\
\end{aligned}
$$

Since $e^{-\frac{y^{2}}{2 \sigma^{2}}}$ is an even function, therefore 
$$\int_{-\infty}^{\infty} e^{\frac{y^{2}}{2 \sigma^{2}}} d y=2 \int_{0}^{\infty} e^{-\frac{y^{2}}{2 \sigma^{2}}} d y$$
Since $y e^{-\frac{y^{2}}{2 \sigma^{2}}}$ is an odd
function, therefore 
$$\int_{-\infty}^{\infty} y e^{\frac{y^{2}}{2 \sigma^{2}}} d y=0$$
Therefore, the integral becomes
$$
\langle x\rangle=\frac{2 \mu}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{0}^{\infty} e^{-\frac{y^{2}}{2 \sigma^{2}}} d y
$$
Put $\frac{y^{2}}{2 \sigma^{2}}=z,$ then $2 y d y=2 \sigma^{2} d z \cdot$ This implies $d y=\frac{\sigma^{2}}{y} d z,$ that is, 
$$d y=\frac{\sigma}{\sqrt{2}} z^{-\frac{1}{2}} d z$$
As $y \rightarrow 0, \  z \rightarrow 0$ and $y \rightarrow \infty, \  z \rightarrow \infty$. Therefore
$$
\begin{aligned}
\langle x\rangle&=\frac{2 \mu}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{0}^{\infty} e^{\frac{y^{2}}{2 \sigma^{2}}} d y \\
&=\frac{2 \mu}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{0}^{\infty} e^{-z} \frac{\sigma}{\sqrt{2}} z^{-\frac{1}{2}} d z \\
&=\frac{2 \mu}{\sigma(2 \pi)^{\frac{1}{2}}} \cdot \frac{\sigma}{\sqrt{2}} \int_{0}^{\infty} e^{-z} z^{\frac{1}{2}-1} d z \\
&=\frac{2 \mu}{\sigma(2 \pi)^{\frac{1}{2}}} \cdot \frac{\sigma}{\sqrt{2}} \Gamma\left(\frac{1}{2}\right) \\
&=\frac{2 \mu}{\sigma(2 \pi)^{\frac{1}{2}}} \cdot \frac{\sigma}{\sqrt{2}} \sqrt{\pi} \\
&=\frac{2 \mu}{\sigma(2 \pi)^{\frac{1}{2}}} \cdot \frac{\sigma}{\sqrt{2}} \sqrt{\pi} \\
&=\mu \\
\end{aligned}
$$

$\boxed{\textbf{Solution}}$ For $(b)$ we start saying
$$
\left\langle x^{2}\right\rangle=\int_{0}^{\infty} x^{2} f(x) d x
$$
$$
=\int_{-\infty}^{\infty} x^{2} \cdot \frac{1}{\sigma(2 \pi)^{\frac{1}{2}}} \exp \left[-\frac{(x-\mu)^{2}}{2 \sigma^{2}}\right] d x
$$
$$
=\frac{1}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{-\infty}^{\infty} x^{2} e^{\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x
$$
Put $x-\mu=y .$ Then $d x=d y .$ As $x \rightarrow 0, \  y \rightarrow 0$ and $x \rightarrow \infty, \  y \rightarrow \infty$.
$$
\begin{aligned}
\left\langle x^{2}\right\rangle&=\frac{1}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{-\infty}^{\infty} x^{2} e^{-\frac{(x-\mu)^{2}}{2 \sigma^{2}}} d x \\
&=\frac{1}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{-\infty}^{\infty}(\mu+y)^{2} e^{-\frac{y^{2}}{2 \sigma^{2}}} d y \\
&=\frac{1}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{-\infty}^{\infty}\left(\mu^{2}+2 \mu y+y^{2}\right) e^{\frac{y^{2}}{2 \sigma^{2}}} d y \\
&=\frac{\mu^{2}}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{-\infty}^{\infty} e^{-\frac{y^{2}}{2 \sigma^{2}}} d y+\frac{2 \mu}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{-\infty}^{\infty} y e^{-\frac{y^{2}}{2 \sigma^{2}}} d y+\frac{1}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{-\infty}^{\infty} y^{2} e^{-\frac{y^{2}}{2 \sigma^{2}}} d y
\end{aligned}
$$

Since $e^{-\frac{y^{2}}{2 \sigma^{2}}}$ is an even function, therefore
$$
\int_{-\infty}^{\infty} e^{-\frac{y^{2}}{2 \sigma^{2}}} d y=2 \int_{0}^{\infty} e^{-\frac{y^{2}}{2 \sigma^{2}}} d y
$$
Since $y e^{-\frac{y^{2}}{2 \sigma^{2}}}$ is an odd function, therefore
$$
\int_{-\infty}^{\infty} y e^{-\frac{y^{2}}{2 \sigma^{2}}} d y=0
$$
Since $y e^{-\frac{y^{2}}{2 \sigma^{2}}}$ is an odd function, therefore
$$
\int_{-\infty}^{\infty} y^{2} e^{-\frac{y^{2}}{2 \sigma^{2}}} d y=2 \int_{0}^{\infty} y^{2} e^{-\frac{y^{2}}{2 \sigma^{2}}} d y
$$
Therefore the above integral becomes
$$
\left\langle x^{2}\right\rangle=\frac{2 \mu^{2}}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{0}^{\infty} e^{\frac{y^{2}}{2 \sigma^{2}}} d y+\frac{2}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{0}^{\infty} y^{2} e^{\frac{y^{2}}{2 \sigma^{2}}} d y
$$
Put $\frac{y^{2}}{2 \sigma^{2}}=z,$ then $2 y d y=2 \sigma^{2} d z$. This implies $d y=\frac{\sigma^{2}}{y} d z,$ that is, $d y=\frac{\sigma}{\sqrt{2}} z^{-\frac{1}{2}} d z$
As $y \rightarrow 0, \  z \rightarrow 0$ and $y \rightarrow \infty, \  z \rightarrow \infty$. Therefore
$$
\begin{aligned}
\left\langle x^{2}\right\rangle&=\frac{2 \mu^{2}}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{0}^{\infty} e^{\frac{y^{2}}{2 \sigma^{2}}} d y+\frac{2}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{0}^{\infty} y^{2} e^{\frac{y^{2}}{2 \sigma^{2}}} d y \\
&=\frac{2 \mu^{2}}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{0}^{\infty} e^{-z} \cdot \frac{\sigma}{\sqrt{2}} z^{\frac{1}{2}} d z+\frac{2}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{0}^{\infty} 2 \sigma^{2} z e^{-z} \cdot \frac{\sigma}{\sqrt{2}} z^{-\frac{1}{2}} d z \\
&=\frac{2 \mu^{2}}{\sigma(2 \pi)^{\frac{1}{2}}} \cdot \frac{\sigma}{\sqrt{2}} \int_{0}^{\infty} e^{-z} z^{\frac{1}{2}} d z+\frac{2 \sqrt{2} \sigma^{3}}{\sigma(2 \pi)^{\frac{1}{2}}} \int_{0}^{\infty} e^{-z} z^{\frac{1}{2}} d z \\
&=\frac{\mu^{2}}{\sqrt{\pi}} \int_{0}^{\infty} e^{-z} z^{\frac{1}{2}-1} d z+\frac{2 \sigma^{2}}{\sqrt{\pi}} \int_{0}^{\infty} e^{-z} z^{\frac{3}{2}-1} d z \\
&=\frac{\mu^{2}}{\sqrt{\pi}} \Gamma\left(\frac{1}{2}\right)+\frac{2 \sigma^{2}}{\sqrt{\pi}} \Gamma\left(\frac{3}{2}\right) \\
&=\frac{\mu^{2}}{\sqrt{\pi}} \cdot \sqrt{\pi}+\frac{2 \sigma^{2}}{\sqrt{\pi}} \cdot \frac{1}{2} \sqrt{\pi} \\
&=\mu^{2}+\sigma^{2} \\
\end{aligned}
$$

So the standard deviation 
$$\left(\left\langle x^{2}\right\rangle-\langle x\rangle^{2}\right)^{\frac{1}{2}}=\left(\mu^{2}+\sigma^{2}-\mu^{2}\right)^{\frac{1}{2}}$$
$$\left(\left\langle x^{2}\right\rangle-\langle x\rangle^{2}\right)^{\frac{1}{2}}=\sqrt{\sigma^{2}}$$
$$\left(\left\langle x^{2}\right\rangle-\langle x\rangle^{2}\right)^{\frac{1}{2}}=\sigma$$




\boxed{\textbf{13.1.21}}
For the gamma distribution
$$
f(x)=\left\{\begin{array}{ll}
\dfrac{1}{\beta^{\alpha} \Gamma(\alpha)} x^{\alpha-1} e^{-x / \beta}, & x>0 \vspace{3mm}\\
0, & x \leq 0
\end{array}\right.
$$

* $\langle x\rangle,$ the mean value of $x,$ is equal to $\alpha \beta$
* $\sigma^{2},$ its variance, defined as $\left\langle x^{2}\right\rangle-\langle x\rangle^{2},$ has the value $\alpha \beta^{2}$



$\boxed{\textbf{Solution}}$ For $(a)$ the mean

$$
\begin{aligned}
\langle x\rangle&=\int_{0}^{\infty} x f(x) d x \\
&=\int_{0}^{\infty} x \cdot \frac{1}{\beta^{a} \Gamma(\alpha)} x^{a-1} e^{-\frac{x}{\beta}} d x \\
&=\frac{1}{\Gamma(\alpha)} \int_{0}^{\infty}\left(\frac{x}{\beta}\right)^{a} e^{-\frac{x}{\beta}} d x 
\end{aligned}
$$

Put $\frac{x}{\beta}=z .$ Then $d x=\beta d z .$ As $x \rightarrow 0, \  z \rightarrow 0$ and $x \rightarrow \infty, \  z \rightarrow \infty$.

$$
\begin{aligned}
\langle x\rangle&=\frac{1}{\Gamma(\alpha)} \int_{0}^{\infty} z^{a} e^{-z} \beta d z \\
&=\frac{\beta}{\Gamma(\alpha)} \int_{0}^{\infty} z^{(a+1)-1} e^{-z} d z \\
&=\frac{\beta}{\Gamma(\alpha)} \Gamma(\alpha+1) \\
&=\frac{\beta}{\Gamma(\alpha)} \cdot \alpha \Gamma(\alpha) \\
&=\alpha \beta \\
\end{aligned}
$$

$\boxed{\textbf{Solution}}$ For $(b)$ 

$$
\begin{aligned}
\left\langle x^{2}\right\rangle&=\int_{0}^{\infty} x^{2} f(x) d x \\
&=\int_{0}^{\infty} x^{2} \cdot \frac{1}{\beta^{a} \Gamma(\alpha)} x^{\alpha-1} e^{-\frac{x}{\beta}} d x \\
&=\frac{\beta}{\Gamma(\alpha)} \int_{0}^{\infty}\left(\frac{x}{\beta}\right)^{\alpha+1} e^{-\frac{x}{\beta}} d x \\
\end{aligned}
$$

Put $\frac{x}{\beta}=z .$ Then $d x=\beta d z .$ As $x \rightarrow 0, \  z \rightarrow 0$ and $x \rightarrow \infty, \  z \rightarrow \infty$
$$
\begin{aligned}
\left\langle x^{2}\right\rangle&=\frac{\beta}{\Gamma(\alpha)} \int_{0}^{\infty} z^{a+1} e^{-z} \beta d z \\
&=\frac{\beta^{2}}{\Gamma(\alpha)} \int_{0}^{\infty} z^{(\alpha+2)-1} e^{-z} d z \\
&=\frac{\beta^{2}}{\Gamma(\alpha)} \Gamma(\alpha+2) \\
&=\frac{\beta^{2}}{\Gamma(\alpha)} \cdot(\alpha+1) \alpha \Gamma(\alpha) \\
&=\alpha(\alpha+1) \beta^{2} \\
&=\alpha^{2} \beta^{2}+\alpha \beta^{2} \\
\end{aligned}
$$

Hence variance, 
$$\sigma^{2}=\left\langle x^{2}\right\rangle-\langle x\rangle^{2}$$
$$=\alpha^{2} \beta^{2}+\alpha \beta^{2}-\alpha^{2} \beta^{2}$$
$$=\alpha \beta^{2}$$




Stirling's Series
-------------------

$\boxed{\textbf{13.4.1}}$

Rewrite Stirling's series to give $\Gamma(z+1)$ instead of $\ln \Gamma(z+1)$
$$
\text { ANS. } \quad \Gamma(z+1)=\sqrt{2 \pi} z^{z+1 / 2} e^{-z}\left(1+\frac{1}{12 z}+\frac{1}{288 z^{2}}-\frac{139}{51,840 z^{3}}+\cdots\right)
$$


$\boxed{\textbf{Solution}}$ Consider the Stirling's formula: 
$$\ln \Gamma(z+1)=\frac{1}{2} \ln 2 \pi+\left(z+\frac{1}{2}\right) \ln z-z+\sum_{n=1}^{\infty} \frac{B_{2 n}}{2 n(2 n-1) z^{2 n-1}}$$
Where $B_{2 n}$ are the Bernoulli's numbers. Use the first few Bernoulli's numbers and rewrite the above Stirling's formula as equivalent to
$$\ln \Gamma(z+1) \sim \frac{1}{2} \ln (2 \pi)+\left(z+\frac{1}{2}\right) \ln z-z+\frac{1}{12 z}-\frac{1}{360 z^{2}}+\frac{1}{1260 z^{3}}-\ldots$$
The Stirling's formula can be rewritten using Gamma function as follows.
Let us take exponential form and collect similar terms to get equivalent form as follows.
$$
\Gamma(z+1) \sim \sqrt{2 \pi}+z^{\left(z+\frac{1}{2}\right)} e^{-z}\left(1+\frac{1}{12 z}+\frac{1}{288 z^{2}}-\frac{139}{51840 z^{3}}+\ldots\right)
$$
Hence, the required result is $$\Gamma(z+1) \sim \sqrt{2 \pi}+z^{\left(z+\frac{1}{2}\right)} e^{-z}\left(1+\frac{1}{12 z}+\frac{1}{288 z^{2}}-\frac{139}{51840 z^{3}}+\ldots\right)$$


$\boxed{\textbf{13.4.5}}$ Test the convergence
$$
\sum_{p=0}^{\infty}\left[\frac{\Gamma\left(p+\frac{1}{2}\right)}{p !}\right]^{2} \frac{2 p+1}{2 p+2}=\pi \sum_{p=0}^{\infty} \frac{(2 p-1) ! !(2 p+1) ! !}{(2 p) ! !(2 p+2) ! !}
$$
This series arises in an attempt to describe the magnetic field created by and enclosed by a current loop.

$\boxed{\textbf{Solution}}$ Consider the series obtained in the magnetic field created by and enclosed by a current loop:
$$
\sum_{p=0}^{\infty} \frac{\Gamma\left(p+\frac{1}{2}\right)}{p !}\left(\frac{2 p+1}{2 p+2}\right)=\pi \sum_{p=0}^{\infty} \frac{(2 p-1) ! !(2 p+1) ! !}{(2 p) ! !(2 p+2) ! !}
$$
Now, we will test the convergence of the series using Stirling asymptotic formula given by
$$
\Gamma(z+1) \sim \sqrt{2 \pi} z^{z+\frac{1}{2}} e^{-z}
$$
$$
\frac{\Gamma\left(p+\frac{1}{2}\right)}{\Gamma(p+1)} \sim \sqrt{e} \frac{\left(\frac{p+\frac{1}{2}}{p+1}\right)^{p+\frac{1}{2}}}{\Gamma(p+1)}
$$
$$
=\frac{\text { constant }}{\Gamma(p+1)}
$$
Hence, the series converges.

$\boxed{\textbf{13.4.6}}$ Show that 
$$\lim _{x \rightarrow \infty} x^{b-a} \frac{\Gamma(x+a+1)}{\Gamma(x+b+1)}=1$$

$\boxed{\textbf{Solution}}$ For a large $\mathrm{n}$, the Stirling asymptotic formula can be taken to the $\mathrm{n}$ arbitrary closed to infinite
Then the expression has asymptotic limit.
$$\ln \left[\left(x^{b-a}\right) \frac{\Gamma(x+a+1)}{\Gamma(x+b+1)}\right]$$
$$=(b-a) \ln x\left(\frac{\Gamma(x+a+1)}{\Gamma(x+b+1)}\right)$$
$$=(b-a) \ln (x)+\ln \left(\frac{\Gamma(x+a+1)}{\Gamma(x+b+1)}\right)$$
$$=(b-a) \ln (x)+\ln \Gamma(x+a+1)-\ln \Gamma(x+b+1)$$
Now we use 
$$
\ln \Gamma(z+1)=\left(z+\frac{1}{z}\right) \ln z-z
$$
Now, $(b-a) \ln (x)+\ln \Gamma(x+a+1)-\ln \Gamma(x+b+1)$ it reduces to
$$
(b-a) \ln (x)+\ln \Gamma(x+a+1)-\ln \Gamma(x+b+1)
$$
$$
-(x+a)-\left(x+b+\frac{1}{2}\right) \ln (x+b)+(x+b)
$$
$$
=(b-a) \ln (x)+(a-b) \ln (x)
$$
Rewrite the $\ln (x+a)$ as follows.
$$
\begin{aligned}
\ln (a+x) &=\ln x\left(1+\frac{a}{x}\right) \\
&=\ln x+\ln \left(1+\frac{a}{x}\right) \\
&=\ln x+\frac{a}{x}+\ldots
\end{aligned}
$$
Now rewrite the $\ln (x+b)$
$$
\begin{aligned}
\ln (b+x) &=\ln x\left(1+\frac{b}{x}\right) \\
&=\ln x+\ln \left(1+\frac{b}{x}\right) \\
&=\ln x+\frac{b}{x}+\ldots
\end{aligned}
$$
For large $x$, make all the terms to exponential form. So, that $\exp (0)=1$. Hence, the limit tends to $1 .$
$$
\lim _{x \rightarrow \infty} x^{b-a} \frac{\Gamma(x+a+1)}{\Gamma(x+b+1)}=1
$$


$\boxed{\textbf{13.4.7}}$ Show that 
$$\lim _{n \rightarrow \infty} \frac{(2 n-1) ! !}{(2 n) ! !} n^{1 / 2}=\pi^{-1 / 2}$$
$\boxed{\textbf{Solution}}$ Write the limit expression in factorial notations. Then it is easy to apply the Stirling formula
$$
\lim _{x \rightarrow \infty} \frac{(2 n-1) ! !}{(2 n) ! !} n^{\frac{1}{2}}=\lim _{x \rightarrow \infty} \frac{(2 n) !}{2^{2 n}(n !)^{2}} n^{\frac{1}{2}}
$$
Take logarithm for the limit
$$
\ln \left(\lim _{x \rightarrow \infty} \frac{(2 n-1) ! !}{(2 n) ! !} n^{\frac{1}{2}}\right)=\ln \left(\lim _{x \rightarrow \infty} \frac{(2 n) !}{2^{2 n}(n !)^{2}} n^{\frac{1}{2}}\right)
$$
Consider the right hand side of the above equation and solve.
$$\ln \lim _{n \rightarrow \infty} \frac{(2 n) ! n^{\frac{1}{2}}}{2^{2 n}(n !)^{2}}$$
$$=\lim _{n \rightarrow \infty} \ln (2 n) !+\frac{1}{2} \ln n-2 n \ln 2-2 \ln (n !)$$
$$\quad \frac{\ln (2 \pi)}{2}+\left(2 n+\frac{1}{2}\right) \ln (2 n)-2 n+\frac{\ln n}{2}$$
$$
\approx -2 n \ln 2-\ln (2 \pi)-2\left(n+\frac{1}{2}\right) \ln n+2 n+\ldots
$$
$$\sim-\frac{1}{2} \ln \pi$$
$$=\ln \pi^{-\frac{1}{2}}$$
Substitute the value of right hand side limit
$$\ln \left(\lim _{x \rightarrow \infty} \frac{(2 n-1) ! !}{(2 n) ! !} n^{\frac{1}{2}}\right)=\ln \pi^{-\frac{1}{2}}$$
$$\quad \lim _{x \rightarrow \infty} \frac{(2 n-1) ! !}{(2 n) ! !} n^{\frac{1}{2}}=\pi^{-\frac{1}{2}}$$
Hence, the limit tends to
$$
\lim _{x \rightarrow \infty} \frac{(2 n-1) ! !}{(2 n) ! !} n^{\frac{1}{2}}=\pi^{-\frac{1}{2}}
$$
