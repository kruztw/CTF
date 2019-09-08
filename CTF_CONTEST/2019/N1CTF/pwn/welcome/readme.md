難度 :  :star::star::star:
  

漏洞: <br>
    1. free 後 g_note[idx] 有設成 NULL, 但 g_ptr 沒有, 存在 double free <br><br>
    

解題流程: <br>
    這題要 leak libc 位址有兩個難點 <br>
    1. chunk 的 size 固定為 0x40<br>
    2. 沒有類似 show 的功能 <br>
    突破 1 的方法就是偽造 chunk, 方法大致分兩種<br>
    一. 在 chunk 偽造一塊 chunk 並用 fastbin attack 拿到它<br>
    二. 利用 fastbin attack 拿到 chunk 前面的位址, 直接改寫 chunk 的 header <br>
    第二種方法在有 tcache 的環境下好做許多(因為不檢查 size, 所以不用偽造), 但如果沒有 tcache 則兩種方法是一樣的 <br><br>
    突破 2 的方法就是修改 \_IO_write_base <br>
    另外,在 free 的時候位址要算好,  header + size 的位址必須是合法的 chunk header, 否則會出錯 <br>
    所以總結來講就是先用 fastbin attack 拿到某塊 chunk 的前面位址 (我們稱作 fake chunk)<br>
    透過 fake chunk 修改下面那塊 chunk 的 size 為 0x91 並將其 free 到 unsorted bin <br>
    再部份修改 fd 指到 \_IO_2_1_stdout_ <br>
    修改 stdout leak 出 libc 的位址 <br>
    接著, 計算 one_shot 並寫到 free_hook (此過程仍然是透過 fastbin attack)<br>
    最後 trigger free 就能拿到 shell 了 <br>
    
    
note:
    這題說難不難, 但也沒有簡單到 welcome 的程度, N1CTF 水準真高 <br>
    