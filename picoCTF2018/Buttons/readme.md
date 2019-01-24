```
點入 Button2 時，會被重導到 boo.html (蠻好聽的）
按 F12 在 Network 可看到 button2.php 的 status 為 302 (重導向）

另外，href 的 method 為 get，而 button1 是採用 POST
```
[post 與 get 的差異](https://blog.toright.com/posts/1203/%E6%B7%BA%E8%AB%87-http-method%EF%BC%9A%E8%A1%A8%E5%96%AE%E4%B8%AD%E7%9A%84-get-%E8%88%87-post-%E6%9C%89%E4%BB%80%E9%BA%BC%E5%B7%AE%E5%88%A5%EF%BC%9F.html)

```
解決方法

1.利用 curl 
curl -X POST http://2018shell3.picoctf.com:21579/button2.php

2.利用 burpsuite
將 GET 改成 POST 即可

3.把 button1.php 改成 button2.php ( PUSH ME 的原始碼)



note: 常見 status

200 ok
204 no content
206 partial content

301 moved permanently
302 Found
可理解為原本存在，但被臨時改變位置 (wikipedia)
304 Not modified (資料從 cache 取得）

400 Bad request
401 Unauthorized
403 Forbidden
404 Not Found
405 Method Not Allowed

500 Internal server error
502 Bad Gateway
503 Service Unavailable
504 Gateway Timeout
```
