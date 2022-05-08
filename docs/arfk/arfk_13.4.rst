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
