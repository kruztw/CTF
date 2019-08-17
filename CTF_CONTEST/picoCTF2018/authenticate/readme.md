```
漏洞
1. printf(buf)  存在 format string 
2. flag.txt 為相對路徑

解題流程

透過 format string 將 authenticated 寫成非 0 即可

note
1. printf 的 %n 可將變數寫入之前印出的字元數
   
   例如
   printf("aaa%n", &var) 會將 var 的值寫成 3
   
2. %3$n 代表此 %n 作用在第 3 個參數
   以 printf("aaa%n", &var) 來說
   aaa%n : 是第 0 個參數
   var   : 是第 1 個參數
   
   後面則按調用規定的暫存器順序，再更後面則是 stack

3. 雖然 format string 看似可寫入任意 stack 位址，但距離太遠也不好操作
   因此，我們先將 authenticated 的位址寫到 stack 再利用 %_$n 的方式寫入
   至於是第幾個參數呢？ 不知道，試試看就對了 (實做請見 exp.py)
   
```
