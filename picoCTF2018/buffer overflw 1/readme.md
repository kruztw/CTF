```
漏洞
gets() 不會檢查長度且沒開 canary 保護 => 存在 bof 漏洞

解題流程
透過 gdb 可看出 buf 從 $ebp - 0x28 開始塞 
而 return address 在 $ebp + 0x4
因為 vuln 的 prologue 會先 push ebp
所以 payload = 'a' * 0x28 + 'a'*0x4 + (此處為 return address)
剩下的就是跳到 win 了
透過 gdb 或 objdump 等等方法可找出 win 的位址
在利用 pwntools 的 p32 包成 32 位元 little endian 形式即可

```
