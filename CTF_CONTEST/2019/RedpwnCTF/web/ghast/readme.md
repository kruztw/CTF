![question](https://github.com/dreamisadream/CTF/blob/master/CTF_CONTEST/2019/RedpwnCTF/web/ghast/pic1.png)

漏洞 :<br>
	admin 的 cookie 洩漏, 導致我們能用 admin 的身份登入, 看到一些資訊 <br>
	像是在 /api/things/ 和 /ghasts </br>

想法 :<br>
	flag 在 /api/flag 但必須滿足下面兩個條件 <br>
	1. user.locked == false<br>
	2. user.name === secrets.adminName<br>
	
	條件 1 對於一般使用者都沒這個問題, 但 admin 就不行
	條件 2 彷彿限制使用者必須是 admin, 但事實並非如此, 只要 name 一樣就行了 

	其中, /api/ghasts 和 /api/register 都能創 name
	但 /api/register 會檢查是否和 admin 一樣, 因此我們只能用 /api/ghasts 
	/api/ghasts 由 /ghasts/make 呼叫, 所以只要在 ghasts name 輸入 admin 的 name 就行了
	輸入完網址就會顯示該 user 的 id
	再將 cookie 的 user 改成該 id ，就能在 /api/flag 看到 flag 了

	但問題是 admin 的 name 去哪看 ?
	正如前面所說, 我們有 admin 的 cookie ("guest:0".encode('base64').strip().replace('=', ''))
	因此只要到 /api/things/Z3Vlc3Q6MA 就能看到 admin 的資訊了 (Z3Vlc3Q6MA 為 admin 的 cookie)




