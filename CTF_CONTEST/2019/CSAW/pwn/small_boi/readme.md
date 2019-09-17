# ctf writeup

難度 :  :star::star:
  

漏洞: <br>
    1. 很明顯的 buffer overflow <br><br>
    

解題流程: <br>
    用 syscall 拿 shell 的方法就我所知有兩種<br>
    1. 59: sys_execve (rdi: buf('/bin/sh'), rsi: 0, rdx: 0) <br>
    2. 322: stub_execveat (rsi: buf('/bin/sh'), rdx: 0, rcx: 0)<br>
    但這兩種方法用一般 rop 都沒辦法達成 <br>
    sys_execve 無法控 rdi, stub_execveat 無法控 rdx <br>
    然而這題的 bof 可寫到 0x200 bytes <br>
    因此可用 [SROP](https://www.slideshare.net/AngelBoy1/sigreturn-ori) (SigReturn Oriented Programming) <br>
    