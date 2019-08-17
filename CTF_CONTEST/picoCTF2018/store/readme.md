```
漏洞：
total cost = 1000*number_flags 存在 overflow 

解題流程
total cost 的型態為 int (-2147483648 ~ 2147483647 )
因此只要讓 1000*number_flags > 2147483647
則 total cost 就會變負的
接下來就賺錢買 flag 啦
```
