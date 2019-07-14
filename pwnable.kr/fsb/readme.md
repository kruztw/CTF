漏洞:<br>

    1. print(buf) 存在 fsb 漏洞<br>

解題流程:<br>

首先，我們先去看第幾個參數會被寫到 stack <br>

輸入: aaaa%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p%p 找尋 0x61616161 出現在第幾個 <br>

但遺憾的是，並沒有出現 0x61 ，探究其原因後發現，他是直接將 buf 塞到 stack <br>
因此最基本的攻擊方式 (將位址寫到 stack 再修改該位址的值) 無法達成 <br>

但幸運的是，該漏洞出現在 fsb() ，而不在 main ，因此可利用 ebp chain 攻擊 <br>

```
fsb_ebp -> main_ebp -> 0x0 

透過 fsb_ebp 將 puts_got 寫入 main_ebp
再透過 main_ebp 將 puts_got 寫入想跳的位址

(用 sleep_got 也行，只是從 printf 往下看剛好看到 puts (用 gdb 看))
```

note: <br>
因為位址無法寫入 stack，所以得一次性寫入 (%n) ，這對於 ssh 來說，是辦不太到的(因為會超時)<br>
因此必須先 ssh 過去，將 exp.py 寫在 /tmp ，在執行 <br>


