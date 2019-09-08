難度 :  :star::star:
  

漏洞: <br>
    1.strncmp(pw, _real_pw, len);  len 的長度由 pw 決定 (pw 由使用者輸入) <br>
    2. strcpy(\_target, buf); 長度不一致存在 bof <br><br>
解題流程: <br>
     先用漏洞一 leak 出 random 值 <br>
    接著, 找找 stack 上有沒有可以 leak 出 libc_base 的位址, 將其 copy 到可以 leak 的地方 (random 後面) <br>
    leak 出該位址並計算 one_shot , 並用漏洞二蓋掉 return address <br>
    leave 後即能拿到 shell <br>
    大致上很簡單, 唯一值得提醒的是, check 的 pw 和 vuln 的 buf 會共用同塊記憶體空間 <br>
    因為它們都是接在 main 下方 (低位址處) 的 stack frame <br>
