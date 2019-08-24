  難度 :  :star::star::star:
  
  ![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/HackconCTF/crypto/Ez%20Pz/pic1.png)

![question2]
(https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/HackconCTF/crypto/Ez%20Pz/pic2.png)

解題想法 : <br>
    猜測為 RSA 加密 (因為懂的不多，所以猜 RSA) <br>
    解 RSA 需要 (n, e) <br>
    n 可透過解密 -1 而來  <br>
    e 可透過暴力破解得到 <br>
    c 題目有給 <br>
    最後 m 可透過解密 c\*pow(2, e, n) % n 得到 <br>

note: <br>
* (-1)<sup>d</sup> = n-1  mod n (如果 d 是奇數)
又 ed = 1 mod(phi(n)) 
phi(n) 是偶數 =>ed 是奇數 => d 是奇數 且 e 是奇數

* (c*2<sup>e</sup>)<sup>d</sup> = 2c<sup>d</sup> = 2m (mod(n))
解密不能傳 c , 不然就變水題了 
