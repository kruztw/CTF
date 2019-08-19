![question](https://github.com/dreamisadream/CTF/tree/master/CTF_CONTEST/RedpwnCTF/crypto/Alien%20Transmission/pic1.png)

想法:
	題目說 key 的長度為 38 且用 "։" 隔開 (注意 "։" 不是 ascii 的冒號, 而是 unicode 的 "։") <br>
	因此用 python3 比較好解, 因為 python3 的 ord 和 chr 預設支援 unicode (python2 只有 ascii)<br>

解法:
	先將字串分組, 每組 38 個, ord 後發現有一個數字特別大, 它就是 '։' (其他都在 ascii 範圍) <br>
	將該數字與 '։' xor 就能得到 key<br>
	而 key 就是 flag <br>
