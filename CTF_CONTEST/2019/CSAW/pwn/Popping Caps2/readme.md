# ctf writeup

難度 :  :star::star:
  

漏洞: <br>
    1. free(ptr + idx); 藉由 idx 可 free 任意位址 <br>
    2. free 後沒設成 NULL <br>
    3. read(0,tmp,0xff); 可能存在 heap overflow <br><br>
    

解題流程: <br>
        這題的 bye() 比 Popping Caps 少了 fwrite 和 malloc 但多了 heap overflow <br>
        因此只需要 6 步就能完成修改(但未必會成功 )<br>
        (原先要 free 掉一開始 malloc 那塊, 偽造 chunk header 現在不用了(直接 free 掉整個 tcache_perthread_struct))<br>
        剩下的步驟就跟 Popping Caps 一樣 (改寫 entry 拿到該 chunk 並修改)
        經過測試後, 改 malloc_hook 、free_hook 、[ \_rtld_global+3840 ] 成 one_shot 都失敗 <br>
        但修改 free_hook 成 system 並 free 掉 content 為 '/bin/sh' 的 chunk 可行 <br>