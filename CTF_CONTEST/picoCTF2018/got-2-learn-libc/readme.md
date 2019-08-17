```
漏洞
1. gets
2. memory leak 

解題流程
題目在一開始就給了 puts 的位址，讓我們能算出 libc 的起始位址
透過起始位址能算出 system 的位址，再利用 gets 就能 get shell 了

note
1. ldd 能找到 libc 的版本 (不要忘了要在遠端操作)
2. objdump -T /lib32/libc.so.6 能找到各個 system call 的相對位移
3. 因為 /bin/sh 要放在 system 的第二個參數，所以中間要塞一個 word (以這題來說是 32 bits)

```
