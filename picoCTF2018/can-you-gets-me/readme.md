```
漏洞
1. gets 存在 bof

解題流程
利用 ROP 取得 shell

首先透過 file 可知 gets 為 x86 的 elf 檔
在 x86 的 system call 中
可透過 sys_execve 取得 shell
只要將 eax 設為 0xb, ebx 指向 buf (內含 /bin/sh), ecx、edx 放 0
再呼叫 int 0x80 即可


note
1. rop 取得方式
ROPgadget --binary ./gets

2. buffer 該取哪？
能寫的地方都行，我是取 bss 的位址

3. 如何取得 bss 的位址
在 gdb 下 info address __bss_start 指令

4. /bin/sh 如何寫入 buf
因為 x86 的暫存器只有 32 bits ，所以得分兩次寫入 (詳情請見 exp.py)

```
[x86 system call](https://syscalls.kernelgrok.com/)
