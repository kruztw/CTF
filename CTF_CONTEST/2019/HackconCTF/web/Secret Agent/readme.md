難度 :  :star: 

![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/HackconCTF/web/Secret%20Agent/pic1.png)

想法:
	題目說 Secret Agent 就知道要改 User Agent 了 <br>
	但問題是要改成什麼 ? <br>
	連上去後只看到一行 <br>
	![question2](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/HackconCTF/web/Secret%20Agent/pic2.png)
	合理猜測 UA = d4rkc0de <br>
	弄了好久都沒成功 <br>
	最後看 writeup 發現 UA = Should d4rkc0de make their own browser (／‵Д′)／~ ╧╧ <br>

POC:
	curl -A "Should d4rkc0de make their own browser" http://68.183.158.95/secret_agent/