難度 :  :star::star::star:
  

漏洞: <br>
    1. memcmp(&g_buf, pw, len);  len 的長度超過 pw, 會導致 memory leak
    2. scanf("%232s", box[i]+1); 存在 off-by-one


解題流程: <br>
        利用第二個漏洞將 box[6\*233] 設成 0, 則輸入的長度會變成 (char) 0 - 1 = 0xff  導致 bof<br>
        透過 bof  將 box[7*233] 設成 0xff, 並利用 view leak canary 和 text_base <br>
        再透過 bof 組 rop, 先 puts 再 read 並跳 one_shot <br>
        要注意, g_buf 的位置很靠近 bss 的下界(低位址), 而 puts 和 printf 都會有很多 push 或 sub esp, xxx 可能會導致 segfault <br>
        因此, 我將 rop 往後移 0x50 <br>
        另外, read 時沒有 gadget 控制 rdx, 要用 objdump 去找 <br>
        而在 read 內有 repz ret 可以控制 rip, 因此只要將 rsi 設置在 rsp 的位址, 並寫入 one_shot 就能跳過去了 <br>