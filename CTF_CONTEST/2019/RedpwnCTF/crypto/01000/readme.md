![question](https://github.com/dreamisadream/CTF/tree/master/CTF_CONTEST/2019/RedpwnCTF/crypto/01000/pic1.png)

想法:
	一大堆 01 先轉成 ascii 再說 (bin2ascii)[https://www.rapidtables.com/convert/number/binary-to-ascii.html] <br>
	題目說 : I found this weird service...<br>
	提示說 : Is it even or odd? <br>
	event or odd ?  => (lsb oracle attack)[https://crypto.stackexchange.com/questions/11053/rsa-least-significant-bit-oracle-attack/] <br>

解法:
	此題一開始會給 n, e, c (皆為二進制) <br>
	並根據你的輸入(c1(題目要求用二進制傳)) 計算 m 且回傳 m 的 lsb<br>
	lsb_attack.py 的 partial 實做 lsb oracle attack 的過程<br>
	oracle 用來傳送和接收回傳值 (m 的 lsb)<br>
