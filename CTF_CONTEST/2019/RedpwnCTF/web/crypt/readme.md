![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/RedpwnCTF/web/crypt/pic1.png)

題目:
```javascript
	s = "vdDby72W15O2qrnJtqep0cSnsd3HqZzbx7io27C7tZi7lanYx6jPyb2nsczHuMec";
	host = 'chall.2019.redpwn.net';
	
	f=>btoa(
                          [...btoa(f)].map(s=>String.fromCharCode(s.charCodeAt(0)+(location.host.charCodeAt(0)%location.host.charCodeAt(3)))).join(''))
```

想法:<br>
	1. 在 console 定義 decode (把 + 改成 -), 再輸入 decode(s)<br>
	2. 先 base64decode 再將每個字元減 ord('v')%ord('b') 再 base64decode<br>
	(我忘記當初為什麼要 base64decode , 也許它長得很 base64 吧...)<br>
