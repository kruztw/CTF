![question](https://github.com/dreamisadream/CTF/tree/master/CTF_CONTEST/RedpwnCTF/crypto/Dunce%20Crypto/pic1.png)

題目給定一組密文並說明為[凱薩加密](https://zh.wikipedia.org/wiki/%E5%87%B1%E6%92%92%E5%AF%86%E7%A2%BC)

解法：
	已知明文為 flag{xxx}, 因此可知 offset = ord('m') - ord('f') <br>
	簡單寫個 exp.py 就能解出來了<br>