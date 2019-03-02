```
GET /WebGoat/HttpProxies/intercept-request?changeMe=Requests+are+tampered+easily HTTP/1.1
Host: localhost:8080
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://localhost:8080/WebGoat/start.mvc
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
x-request-intercepted: true
X-Requested-With: XMLHttpRequest
Content-Length: 30
Connection: close
Cookie: JSESSIONID=5CF1D8B7701A763102AED87DA7C13CCB


note:
GET 的參數要加在網址後面
POST 則是分開寫
```
