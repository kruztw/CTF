# ctf writeup

難度 :  :star::star::star::star:
  

漏洞: <br>
1. getId() 的 id 大小為 8 bytes, 而回傳值為 long (4 bytes) , 存在 type overflow<br>

這洞很難找, 因為 ghidra 將 id 的型態寫成 long <br>
ida 就好一點, 寫成 unsignd __int64 , 但也不對, 既然是 unsigned 為什麼不能輸入 -1 <br>
這洞我找了很久, 亂試後偶然發現 (因為本人喜歡用 ghidra, 如果是用 ida 應該很快就能發現) <br><br>
    
解題流程: <br>
先在 g_table[0] 創立一條 linked list (假設有 4 個 node)<br>
=> g_table[0] : a->b->c->d<br><br>

再利用 type overflow load 兩次 <br>
第一次正常 load (load a)<br>
=> g_table[0] : b->c->d->e<br>
=> g_header+8 : a->b->c->d->e<br>
<br>
第二次用 type overflow load g_header+8 的 chain <br>
=> g_table[0] : b->c->d->e <br>
=> g_header+8 : b->c->d->e <br><br>
這時, b 同時出現在兩個地方, 就可以用 uaf 攻擊了 <br>
剩下的就自己摸索吧 <br>