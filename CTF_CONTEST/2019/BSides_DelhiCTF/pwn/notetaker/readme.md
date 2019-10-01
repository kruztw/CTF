# ctf writeup

難度 :  :star::star:
  

漏洞: <br>
```c=
// g_table  0x6020a0
// g_size    0x602100
while (i < 13 && g_table[i]) //bug i 可能等於 13 但最多只能容納 12 個 note
        i = i + 1;
        
if (i != 12){...}
```
因為 g_table 下方連著 g_size, 所以 g_table[12] = g_size[0], 如果 g_size[0] != 0 則 while loop 會因為 i=13 而 break <br>
且 if 的判斷是 i != 12 而非 i >= 12, 所以 g_table[13] = g_size[1] 就會被寫入 heap 的位址, 導致 g_table[1] 有嚴重的 heap overflow
<br><br>
    

解題流程: <br>
先 add 13 次, 並把 chunk 內容寫入 /bin/sh; (因為等等要把 free_got 改成 system) <br>
接著利用 heap overflow 將下一塊 chunk 的 \*description 改成 free_got 的位址 <br>
如此一來修改該塊 chunk 就能改 free_got <br>
將 free_got 改成 puts, leak 出 libc 位址, 再寫入 system <br>
最後 trigger free <br>


<br>