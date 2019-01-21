從原始碼或 burpsuite 可發現存在 hidden 變數 debug<br>
將 debug 值設為 1 即可發現存在 sql injection 漏洞

![image](https://github.com/dreamisadream/CTF/blob/master/picoCTF2018/Irish%20Name%20Repo/irish1.png)

試了幾種後發現
-- 和 ; 可以用
＃ 會出錯

' or 1=1 --
' or 1=1 ;
admin' --
UNION SELECT * FROM users --
