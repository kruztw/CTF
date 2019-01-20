漏洞
func(int key) 裡面使用到 gets 存在 buffer overflow

解題流程

利用 gdb 可以發現 overflowme 在 $ebp - 0x2c 

![image](https://github.com/dreamisadream/CTF/blob/master/pwnable.kr/bof1.png)

因此只要塞超過 0x2c 就可以蓋到 ebp 、return address ...
而 key 的位址在 ebp + 0x8

因此 padload = 'a'*0x2c + 'a'*0x8 + p32(0xcafebabe)

p32 為 pwntools 中一個實用的工具，可以將內容打包成 32-bit little endian 的形式



