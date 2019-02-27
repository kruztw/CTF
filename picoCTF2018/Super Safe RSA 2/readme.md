```
此題考的內容為 Wiener's attack
```
[Wiener's attack](https://sagi.io/2016/04/crypto-classics-wieners-rsa-attack/)

```

使用條件
1. q < p < 2q
2. d < 1/3  N^(1/4)

由 RSA 的兩條公式推導而來
(1) phi(N) = (p-1)(q-1)

乘開後可得 p 的二次式
p^2 + (phi(N) - N - 1)p + N = 0

如果知道 phi(N) 則可求 p 
有 p 有 N 就有 q 就有 d

但...要怎麼知道 phi(N) ??

(2) de - k phi(N) = 1  ( 因為 de = 1 mod ( phi(N) )

同除 d phi(N) 可得 
e/phi(N) - k/d = 1/dphi(N)

因為 1/dphi(N) 很小，所以 e/phi(N) = k/d
由條件 2 ，可將 e/phi(N) 用 e/N 近似 (詳情請見維基百科的證明)

將 e/N 用連分式近似，並令分子為 k 分母為 d ( ex e/N = 2/3   => k = 2, d = 3)
代入上式可得 phi(N)

再將 phi(N) 代入 p 的二次式可得 p q
若解出來 p q 不是質數，則代下一個 e/N 

(維基百科的 example)[https://en.wikipedia.org/wiki/Wiener%27s_attack]

note
29/146 = 1/(5 + 1/29)
```
[Manan Pal Singh 大大的程式碼](https://gist.github.com/mananpal1997/73d07cdc91d58b4eb5c818aaab2d38bd)
