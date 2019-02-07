```
漏洞
1. flag 為相對路徑
2. printf(buf) 存在 format string 漏洞

解題流程

x64 使用 rdi, rsi, rdx, rcx, r8, r9 儲存參數(左至右)，多於 6 個時，右至左塞入 stack

ex:
foo(a1, a2, a3, a4, a5, a6, a7, a8)

push a8
push a7
r9 : a6
r8 : a5
rcx: a4
rdx: a3
rsi: a2
rdi: a1


另外，printf("%3$s")
可查看 printf 第 3 個參數的內容 
也就是 rcx 的值 (準確來說應該是 rcs 指到的位址的內容，因為是 %s)
為什麼是 rcx 呢？
因為 rdi 為編號 0 的參數
也就是 "%3$s" 儲存在 rdi 為第 0 個參數，即 %0$s 會印出 %0$s

又因為 while 前一行才 fgets flag 
因此，我們合理猜測 flag 應該在距離 sp 不遠處
經由測試後發現，利用 %8$s 即可印出 flag
```
