難度 :  :star::star:
  

漏洞: <br>
    1. idx 可以是負的 (out of bound read write)  <br><br>
    

解題流程: <br>
    idx < 0 的情況可以 leak 和 write got, 且沒開 NX <br>
    因此這題很明顯屬於 return to shellcode 類型 <br>
    差別在於 shellcode 必須是 printable 且長度要 < 80 <br>
    事實上製造 printable shellcode 一點都不難 <br>
    因為我們的目標很簡單, 就是 execve("/bin/sh") <br>
    在 32 位元下, 只要照 [system call 格式](https://syscalls.kernelgrok.com) 將暫存器填入正確的值, 再執行 int 0x80 就能 get shell 了 <br>
    eax, ecx, edx 都很好控, 麻煩的在 ebx 和 int 0x80 <br>
    好在 ebx 可透過 free(note[0]) , note[0] == "/bin/sh" 取得 <br>
    所以真正的問題出在 int 0x80 <br>
    int 0x80 的機器碼為 dc 80, 兩個都是不可打印字元 <br>
    但我們可以透過 xor and add sub 方式湊成 <br>
    方法很多, exp.py 只是其中一種 <br>