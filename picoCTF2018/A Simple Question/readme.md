```

SQL query: SELECT * FROM answers WHERE answer=''
原本看到這行以為是簡單的 SQL injection
輸入 ' or 1=1 -- 後發現沒這麼單純

網頁顯示 You are so close.
而當 1=2 時則顯示 WRONG

看來這題比較像是 bind injection
因此我們透過 UNION SELECT * FROM answers WHERE answer='a%'--

如果顯示 You are so close. 代表答案為 a 開頭
如果顯示 Wrong 則不是
如此繼續...我們就能找出 answer 了
```
