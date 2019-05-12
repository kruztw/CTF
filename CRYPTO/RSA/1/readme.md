題目來源 : midnightsunctf/Open-gyckel-krypto<br>
[參考 writeup](https://upbhack.de/posts/2019/04/writeup-open-gyckel-krypto-from-midnightsun-ctf-2019-quals/)

解題方法:

p = a * 10<sup>250</sup> + b</br>
q = b * 10<sup>250</sup> + a

N = pq = ab * 10<sup>500</sup> + (a<sup>2</sup> + b<sup>2</sup>) * 10<sup>250</sup> + ab

令 ab = x , a<sup>2</sup> + b<sup>2</sup> = y

=> N = x * 10<sup>500</sup> + y * 10<sup>250</sup> + x

示意圖 (每一字元代表 250 位)
```
  x1x2
    y1y2
+)    x1x2
---------
  N1N2N3N4
``` 

x = (N1 - carry) * 10<sup>250</sup> + N4    (carry 來自 x2 + y1 的進位 ，頂多 1 2 ) </br>
y = ( N - x * 10<sup>250</sup> - x ) / 10 <sup>250</sup>

phi(N) = (p-1)(q-1) = N - (p+q) + 1

p + q = (a+b) * 10<sup>250</sup> + (a+b)</br>
a + b = 根號(a+b)<sup>2</sup> = 根號(2x + y)

代入得到 phi(N) 即可求 d , 即可解 m

