```
此題考 RSA 多個質數分解

常見的 RSA 的 n 為 2 個質數 (p, q) 相乘
但為了速度起見，n 可由多個質數 (p1, p2, ..., pk) 相乘 (速度變成 k^2 倍)
且計算方式與 2 個質數的 RSA 相同
唯獨差在 phi(n) = (p1-1)(p2-1)...(pk-1)   

而這題的問題出在 n 分解後的質數太小
導致 n 很容易分解
這相當於暴露原 RSA 的 p, q
我們利用過去的 code 即可得到 flag

note:
```
[質因數分解](https://www.alpertron.com.ar/ECM.HTM)
