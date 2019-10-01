# ctf writeup

難度 :  :star::star:
  

漏洞: <br>
    1. delete 後, 沒把 g_table[idx] 設成 NULL (存在 uaf ) <br><br>
    

解題流程: <br>
利用 fastbin attack 修改 malloc_hook 為 one_shot <br>